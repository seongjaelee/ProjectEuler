import problem
import math
import sys

class Problem(problem.Problem):
	def __init__(self):
		number = 26
		question = 'Find the value of d < 1000 for which 1/d contains the longest recurring cycle.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def nCycle(n):
			while n % 2 == 0:
				n /= 2
			while n % 5 == 0:
				n /= 5
			if n == 1:
				return 0
			
			m = 10
			ret = 1	
			while (m - 1) % n != 0:
				ret += 1
				m *= 10
			return ret
			
		assert nCycle(6) == 1
		assert nCycle(7) == 6
		assert nCycle(8) == 0
		assert nCycle(9) == 1
		assert nCycle(10) == 0
		
		ret = 1
		maxCycle = 0
		for i in xrange(1, 1000):
			c = nCycle(i)
			if c > maxCycle:
				ret = i
				maxCycle = c
				
		return ret