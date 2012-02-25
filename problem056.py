import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 56
		question = 'Considering natural numbers of the form, a^b, finding the maximum digital sum.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def mul(a, b):
			for i in xrange(len(a)):
				a[i] *= b
			for i in xrange(len(a) - 1):
				a[i+1] += a[i] / 10
				a[i] %= 10
			while a[-1] >= 10:
				a.append(a[-1]/10)
				a[-2] %= 10
			return a
		
		ret = 0
		for i in xrange(2, 100):
			a = mul([i], 1)
			for j in xrange(99):
				ret = max(ret, sum(a))
				a = mul(a, i)
		return ret