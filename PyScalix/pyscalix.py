import sqlite3
import csv
import os


class Convert:

    @staticmethod
    def SqltoCsv(databasefile, tablename):
        '''
        SqltoCsv takes a database file and table name as an input
        '''
        flag = False
        try:

            conn = sqlite3.connect(databasefile)
            c = conn.cursor()
            c.execute(f"SELECT * FROM {tablename}")
            with open(tablename+".csv", 'w', newline='', encoding='utf8') as f:
                writer = csv.writer(f)
                writer.writerow([d[0] for d in c.description])
                writer.writerows(c)
            c.close()
            conn.close()
            flag = True
        except:
            flag = False
        return flag

    @staticmethod
    def CsvtoSql(csvfile):
        '''
        CsvtoSql takes a Csv file as an input\n
        Poor formated csv will raise an exception
        '''
        exception = 1
        flag = False
        try:
            table_name = os.path.basename(csvfile).split('.')[
                0].replace(" ", "_")
            dbfile = table_name+".sqlite"
            if os.path.exists(dbfile):
                os.remove(dbfile)
            conn = sqlite3.connect(dbfile)
            cursor = conn.cursor()
            with open(csvfile, 'r', encoding='utf-8') as file:
                for n, line in enumerate(file):
                    columns = line.strip().split(',')
                    if n == 0:
                        if columns[-1] == "":
                            cursor.execute(
                                f'CREATE TABLE {table_name} ({", ".join(columns[:-1])})')
                        else:
                            cursor.execute(
                                f'CREATE TABLE {table_name} ({", ".join(columns)})')
                    else:
                        if columns[-1] == "":
                            try:
                                exception += 1
                                cursor.execute(
                                    f"INSERT INTO {table_name} VALUES ({','.join('?' * (len(columns)-1))})", line.strip().split(',')[:-1])
                            except Exception as e:
                                print("Exception occured at line",
                                      exception, '\n'.e)
                        else:
                            try:
                                exception += 1
                                cursor.execute(
                                    f"INSERT INTO {table_name} VALUES ({','.join('?' * len(columns))})", line.strip().split(','))
                            except Exception as e:
                                print("Exception occured at line",
                                      exception, '\n', e)
                conn.commit()
                flag = True
        except Exception as e:
            print(e)
            flag = False
        return flag
