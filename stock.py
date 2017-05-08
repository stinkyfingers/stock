import csv
import os

# data from: https://quantquote.com/historical-stock-data

class Data():
	def __init__(self, directory=''):
		self.dir=directory
		self.corporations=[]
		self.limit=10

	def importDir(self):
		for subdir, dirs, files in os.walk(self.dir):
			for i, file in enumerate(files):
				if i >= self.limit:
					return
				filepath = subdir + os.sep + file
				corporation=Corporation(path=filepath)
				corporation.parseNameFromPath()
				corporation.importCsv()
				self.corporations.append(corporation)


class Corporation():
	def __init__(self, path='', name=''):
		self.name=name
		self.path=path
		self.records=[]

	def importCsv(self):
		with open(self.path) as file:
			reader = csv.reader(file, delimiter=',')

			for row in reader:
				self.records.append(Record(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

	def parseNameFromPath(self):
		path=self.path
		try:
			start=self.path.rindex('table_') + len('table_')
		except:
			start=0

		try:
			end=self.path.rindex('.csv')
		except:
			end=len(self.path)

		self.name=path[start:end]


class Record():
	def __init__(self, date='', mystery='', ytdhi='', ytdlo='', hi='', lo='', vol=''):
		self.date=date
		self.myster=mystery
		self.ytdhi=ytdhi
		self.ytdlo=ytdlo
		self.hi=hi
		self.lo=lo 
		self.vol=vol
