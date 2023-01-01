import PyScalix
import unittest


class Test(unittest.TestCase):

    def test_toCsv(self):
        self.assertEqual(PyScalix.SqltoCsv(
            "data/sampleStates.sqlite", "sampleStates"), True)

    def test_toSqlite(self):
        self.assertEqual(PyScalix.CsvtoSql("data/sampleStates.csv"), True)


if __name__ == "__main__":
    unittest.main()
