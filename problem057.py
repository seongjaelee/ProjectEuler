import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 57
		question = 'Investigate the expansion of the continued fraction for the square root of two.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def add(a, b):
			ret = []
			for i in xrange(max(len(a), len(b))):
				if i < len(a) and i < len(b):
					ret.append(a[i] + b[i])
				elif i < len(a):
					ret.append(a[i])
				else:
					ret.append(b[i])
			for i in xrange(len(ret)-1):
				ret[i+1] += ret[i] / 10
				ret[i] = ret[i] % 10
			while ret[-1] >= 10:
				ret.append(ret[-1] / 10)
				ret[-2] = ret[-2] % 10
			return ret
			
		def f(a, b):
			c = add(a, b)
			d = add(c, b)
			return d, c
		
		ret = 0
		i = 1
		a, b = [3], [2]
		while i < 1000:
			i += 1
			a, b = f(a, b)
			if len(a) != len(b):
				ret += 1
		return ret