import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 40
		question = 'Finding the nth digit of the fractional part of the irrational number.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def getNDigits(n):
			return len(str(i))
		
		nDigits = 0
		i = 1
		d = 1
		ret = 1
		while True:
			j = getNDigits(i)
			if d <= nDigits + j:
				ret *= int(str(i)[d - nDigits - 1])
				d *= 10
			nDigits += j
			i += 1
			if d == 10000000:
				break
		return ret