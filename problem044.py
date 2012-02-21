import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 44
		question = 'Find the smallest pair of pentagonal numbers whose sum and difference is pentagonal.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):

		pentagonals = [1, 5]
		
		def getPentagonal(n):
			return n*(3*n-1)/2
			
		# 3n^2 - n = 2x
		# 3n^2 - n - 2x = 0
		# n = [-b +- sqrt(b^2 - 4ac)] / 2a
		def isPentagonal(n):
			m = (math.sqrt(24 * n + 1) + 1) / 6
			return int(m) == m
		
		def isValid(n, m): # n < m
			return isPentagonal(m-n) and isPentagonal(m+n)
		
		ret = 0
		n = 2
		while True:
			x = pentagonals[-1]
			for i in xrange(n-1, -1, -1):
				y = pentagonals[i]
				if ret != 0 and x - y >= ret:
					break
				if isValid(y, x):
					ret = x - y
			n += 1
			pentagonals.append(getPentagonal(n))
			if ret != 0 and pentagonals[-1] - pentagonals[-2] >= ret:
				break
		return ret