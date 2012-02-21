import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 38
		question = 'What is the largest 1 to 9 pandigital that can be formed by multiplying a fixed number by 1, 2, 3, ... ?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def getConcatenated(n):
			ret = ''
			i = 1
			while len(ret) < 9:
				ret += str(n*i)
				i += 1
			return ret
		
		def isPandigital(n):
			s = getConcatenated(n)
			if len(s) != 9:
				return False
			for i in xrange(1, 10):
				if str(i) not in s:
					return False
			return True
		
		ret = 0
		for i in xrange(1, 9999):
			if isPandigital(i):
				c = int(getConcatenated(i))
				if ret < c:
					ret = c
		return ret