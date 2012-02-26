import problem
import math
import utility
import itertools
import sys

class Problem(problem.Problem):
	def __init__(self):
		number = 61
		question = 'Find the sum of the only set of six 4-digit figurate numbers with a cyclic property.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def f(i, j):
			return i * ((j - 2) * i - (j - 4)) / 2
			
		def g(n):
			assert 3 <= n and n <= 8
			i = 1
			ret = []
			while True:
				v = f(i, n)
				if v >= 10000:
					break
				if v >= 1000:
					ret.append(v)
				i += 1
			return ret
		
		ngonalNumbers = {}
		for n in xrange(3, 9):
			ngonalNumbers[n] = g(n)
		
		def h(combi, ngonalNumbers):
			candidates = [[str(i)] for i in ngonalNumbers[combi[0]]]
			
			for i in xrange(1, len(combi)):
				newCandidates = []
				for c in candidates:
					for j in ngonalNumbers[combi[i]]:
						if c[-1][2:] == str(j)[:2]:
							newCandidates.append(c + [str(j)])
				candidates = newCandidates
			
			ret = []
			for c in candidates:
				if c[-1][2:] == c[0][:2]:
					ret.append(c)
			return ret
		
		
		for combi in itertools.permutations([4,5,6,7,8]):
			i = h([3] + list(combi), ngonalNumbers)
			if len(i) != 0:
				assert len(i) == 1
				return sum([int(j) for j in i[0]])
		assert False
		return 0