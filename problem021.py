import problem
from utility import *
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 21
		question = 'Evaluate the sum of all amicable pairs under 10000.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		limit = 10000
		primes = getPrimes(limit)
		
		assert sum(getDivisors(220, primes)) - 220 == 284
		assert sum(getDivisors(284, primes)) - 284 == 220
		
		isAmicable = [None for i in xrange(limit)]
		ret = 0
		for i in xrange(1, limit+1):
			if isAmicable[i-1] is None:
				j = sum(getDivisors(i, primes)) - i
				if j < limit and i != j and isAmicable[j-1] == None and sum(getDivisors(j, primes)) - j == i:
					isAmicable[i-1] = True
					isAmicable[j-1] = True
					ret += i + j
				else:
					isAmicable[i-1] = False
		return ret