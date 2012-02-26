import problem
import math
import utility
import itertools
from math import sqrt
from math import floor

class Problem(problem.Problem):
	def __init__(self):
		number = 65
		question = 'Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		e = [2]
		for i in xrange(1, 35):
			e += [1, 2 * i, 1]
		
		def f(a, n):
			nom = e[n-1]
			den = 1
			for i in xrange(1, n):
				tmp = nom
				nom = den + nom * e[n-1-i]
				den = tmp
			return (nom, den)
		
		assert f(e, 1) == (2, 1)
		assert f(e, 2) == (3, 1)
		assert f(e, 3) == (8, 3)
		assert f(e, 4) == (11, 4)
		assert f(e, 5) == (19, 7)
		assert f(e, 6) == (87, 32)
		assert f(e, 7) == (106, 39)
		assert f(e, 10) == (1457, 536)
		assert sum([int(s) for s in str(f(e, 10)[0])]) == 17
		
		return sum([int(s) for s in str(f(e, 100)[0])])