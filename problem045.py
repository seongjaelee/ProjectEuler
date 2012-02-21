import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 45
		question = 'After 40755, what is the next triangle number that is also pentagonal and hexagonal?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):

		# n^2 + n - 2x = 0
		# n = [-1 + sqrt(1 + 8x)] / 2
		def isTriangle(n):
			m = (math.sqrt(8*n+1) - 1) / 2
			return int(m) == m
		
		# 3n^2 - n - 2x = 0
		# x = [-b +- sqrt(b^2 - 4ac)] / 2a
		def isPentagonal(n):
			m = (math.sqrt(24*n+1) + 1) / 6
			return int(m) == m
		
		def getHexagonal(n):
			return n * (2*n-1)
		
		assert isTriangle(getHexagonal(143))
		assert isPentagonal(getHexagonal(143))
		
		n = 144
		while True:
			m = getHexagonal(n)
			if isPentagonal(m) and isTriangle(m):
				return m
			n += 1