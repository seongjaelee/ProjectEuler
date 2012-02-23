import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 33
		question = 'Discover all the fractions with an unorthodox cancelling method.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		count = 0
		nom = 1
		den = 1
		for i in xrange(1, 10):
			for j in xrange(1, 10):
				for k in xrange(1, 10):
					if j >= k:
						continue
					# ij/ik = j/k
					if (10*i + j)*k == (10*i + k)*j:
						den *= k
						nom *= j
						count += 1
					# ij/ki = j/k
					if (10*i + j)*k == (10*k + i)*j:
						den *= k
						nom *= j
						count += 1
					# ji/ik = j/k
					if (10*j + i)*k == (10*i + k)*j:
						den *= k
						nom *= j
						count += 1
					# ji/ki = j/k
					if (10*j + i)*k == (10*k + i)*j:
						den *= k
						nom *= j
						count += 1
		assert count == 4

		for i in xrange(nom, 1, -1):
			if den % i == 0:
				return den / i
		return den