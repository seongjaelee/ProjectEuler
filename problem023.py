import problem
from utility import *
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 23
		question = 'Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		limit = 28123

		def isAbundant(n):
			return n < sum(getDivisors(n)) - n

		assert sum(getDivisors(28)) - 28 == 28

		isAbundantList = [isAbundant(i) for i in xrange(1, limit + 1)]
		
		for i in xrange(1, 12):
			assert isAbundantList[i-1] == False
		assert isAbundantList[12-1]
		
		def isSummedWithAbundants(n):
			for j in xrange(1, n):
				if isAbundantList[j-1] and isAbundantList[n-j-1]:
					return True
			return False
		
		for i in xrange(1, 24):
			assert isSummedWithAbundants(i) == False
		assert isSummedWithAbundants(24)
		
		ret = 0
		for i in xrange(1, limit):
			if not isSummedWithAbundants(i):
				ret += i
		return ret