import unittest
import stock

class TestCsvToData(unittest.TestCase):
	def test_corporation(self):
		path='./data/daily/table_a.csv'
		c=stock.Corporation(path)
		c.parseNameFromPath()
		c.importCsv()
		self.assertEqual(c.name, 'a')
		self.assertEqual(c.path, path)
		self.assertEqual(len(c.records), 3452)

	def test_data(self):
		directory='./data'
		d=stock.Data(directory=directory)
		d.importDir()
		self.assertEqual(len(d.corporations), 10)



if __name__ == '__main__':
	unittest.main()