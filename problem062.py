import problem
import math
import utility
import itertools
import sys

class Problem(problem.Problem):
	def __init__(self):
		number = 62
		question = 'Find the smallest cube for which exactly five permutations of its digits are cube.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		
		def f(nDigits):
			# 10^n-1 <= x^3 < 10^n
			# (n-1) log10 <= 3 logx < n log 10 
			# exp((n-1) / 3 * log10) <= x < exp(n / 3 * log10)
			n = nDigits
			v = math.exp(math.log(10) * (n-1) / 3.0)
			for i in xrange(int(v) - 1, int(v) + 2):
				if len(str(i*i*i)) == nDigits:
					return i
		
		def convertToKeys(n):
			ret = ''
			s = str(n)
			for i in xrange(10):
				ret += str(s.count('%d'%(i)))
			return ret
		
		def g(nDigits):
			minN, maxN = f(nDigits), f(nDigits + 1) - 1
			candidates = [i*i*i for i in xrange(minN, maxN)]
			keys = [convertToKeys(i) for i in candidates]
			for i, k in enumerate(keys):
				if keys.count(k) == 5:
					return candidates[i]
			return None
		
		i = 2
		while True:
			ret = g(i)
			if ret != None:
				return ret
			i += 1