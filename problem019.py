import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 19
		question = 'How many Sundays fell on the first of the month during the twentieth century?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		year = 1900
		month = 1
		date = 1
		day = 0
		
		ret = 0
		while True:
			date += 1
			day += 1
			
			if day == 7:
				day = 0
			
			if month == 12 and date == 32:
				date = 1
				month = 1
				year += 1
			elif month in [1, 3, 5, 7, 8, 10] and date == 32:
				date = 1
				month += 1
			elif month in [4, 6, 9, 11] and date == 31:
				date = 1
				month += 1
			elif month == 2 and year % 4 != 0 and date == 29:
				date = 1
				month += 1
			elif month == 2 and year % 4 == 0 and date == 30:
				date = 1
				month += 1
			
			if date == 1 and day == 6 and year >= 1901:
				ret += 1
			
			if year == 2000 and month == 12 and date == 31:
				break
				
		return ret