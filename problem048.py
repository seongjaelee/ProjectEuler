import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 48
		question = 'Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def getLastTenDigits(n):
			ret = n
			limit = 10000000000
			for i in xrange(n-1):
				ret *= n
				ret %= limit
			return ret
		
		ret = 0
		limit = 10000000000
		for i in xrange(1, 1001):
			ret += getLastTenDigits(i)
		ret %= limit
		return ret