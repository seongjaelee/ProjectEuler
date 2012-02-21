import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 39
		question = 'If p is the perimeter of a right angle triangle, {a, b, c}, which value, for p <= 1000, has the most solutions?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def getNumberOfRightTriangles(n):
			# a*a + b*b == c*c
			# <=> a*a + b*b == (n-c)^2
			# <=> 2n(a+b) == n^2 + 2ab
			
			if n % 2 != 0:
				return 0
			ret = 0
			nnhalf = n*n/2
			for a in xrange(3, int(n/3) + 1):
				for b in xrange(a, int((n-a)/2) + 1):
					if n * (a + b) == nnhalf + a * b:
						ret +=1
			return ret
			
		assert getNumberOfRightTriangles(120) == 3
		
		ret = 0
		maxNSolutions = 0
		for p in xrange(12, 1001):
			nSolutions = getNumberOfRightTriangles(p)
			if maxNSolutions < nSolutions:
				ret = p
				maxNSolutions = nSolutions
		return ret