import problem
import math
import sys
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 28
		question = ''
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def f(n):
			assert n % 2 == 1
			assert n > 1
			x = 1
			ret = 1
			for i in xrange(n/2):
				ret += 4 * x + (i + 1) * 2 * 10
				x += (i + 1) * 2 * 4
			return ret
			
		assert f(5) == 101
		return f(1001)