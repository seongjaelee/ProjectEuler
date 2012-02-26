import problem
import math
import utility
import itertools
from math import sqrt
from math import floor

class Problem(problem.Problem):
	def __init__(self):
		number = 64
		question = 'How many continued fractions for N <= 10000 have an odd period?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def f(n):
			ret = []
			m = 0
			d = 1
			a = int(floor((sqrt(n) + m) / d))
			ret.append((m, d, a))
			
			# (sqrt(n) + m) / d - a
			# = (sqrt(n) + m - ad) / d
			
			# therefore
			# d / (sqrt(n) + m - ad)
			# (sqrt(n) - m + ad) / ((n - (m - ad)^2) / d)
			
			# therefore
			# m' = -m + ad
			# d' = (n - m'^2) / d

			while True:
				m = - m + a * d
				assert (n - m * m) % d == 0
				d = (n - m * m) / d
				a = int(floor((sqrt(n) + m) / d))
				if len(ret) >= 2 and ret[1] == (m, d, a):
					return len(ret) - 1
				ret.append((m, d, a))

		assert f(2) == 1
		assert f(3) == 2
		assert f(5) == 1
		assert f(7) == 4
		assert f(13) == 5
		assert f(23) == 4
		
		ret = 0
		for i in xrange(1, 10001):
			j = int(sqrt(i))
			if j * j == i:
				continue
			if f(i) % 2 == 1:
				ret += 1
		return ret