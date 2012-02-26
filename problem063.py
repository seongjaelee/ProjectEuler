import problem
import math
import utility
import itertools
import sys

class Problem(problem.Problem):
	def __init__(self):
		number = 63
		question = 'How many n-digit positive integers exist which are also an nth power?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		# 10^n-1 <= x^n < 10^n
		# (n-1)log10 <= nlogx < nlog10
		# therefore, x < 9.
		# n(log10 - logx) <= log10
		ret = 0
		for x in xrange(1, 10):
			for n in xrange(1, int(math.log(10) / (math.log(10) - math.log(x))) + 1):
				ret += 1
				assert len(str(pow(x, n))), n
		return ret