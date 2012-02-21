import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 37
		question = 'Find the sum of all eleven primes that are both truncatable from left to right and right to left.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def isTruncatablePrime(n, primes):
			s = str(n)
			l = len(s)
			for i in xrange(1, l):
				if not isPrime(int(s[i:]), primes):
					return False
				if not isPrime(int(s[:-1*i]), primes):
					return False
			return True
	
		limit = 10
		primes = getPrimes(limit)
		ret = 0
		numberOfTruncatablePrimes = 0
		while True:
			limit *= 10
			primes = getPrimesFrom(limit, primes)
			for p in primes:
				if p >= limit / 10 and isTruncatablePrime(p, primes):
					ret += p
					numberOfTruncatablePrimes += 1
				if numberOfTruncatablePrimes == 11:
					break
			if numberOfTruncatablePrimes == 11:
				break

		return ret