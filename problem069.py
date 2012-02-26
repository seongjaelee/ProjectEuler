import problem
import math
import utility
import itertools
from math import sqrt
from math import floor
import fractions

class Problem(problem.Problem):
	def __init__(self):
		number = 69
		question = 'Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def phi2(n):
			ret = 0
			for i in xrange(1, n):
				if fractions.gcd(i, n) == 1:
					ret += 1
			return ret
		
		def getFactors(n, primes):
			sqn = sqrt(n)
			for p in primes:
				if n % p == 0:
					yield p
				if p > sqn:
					break
		
		def phi(n, primes):
			l = [True for i in xrange(n)]
			#factors = utility.factorize(n, primes)[0]
			#for f in factors:
			for f in getFactors(n, primes):
				for i in xrange(n / f):
					l[f * i] = False
			ret = 0
			for i in l:
				if i:
					ret +=1
			return ret
		
		primes = utility.getPrimes(100001)
		
		assert phi(9, primes) == 6
		assert phi(10, primes) == 4
		
		#print 1.0 * phi(6, primes) / 6
		#print 1.0 * phi(6*2, primes) / 6 / 2
		#print 1.0 * phi(10, primes) / 10
		#print 1.0 * phi(30, primes) / 30
		#print 1.0 * phi(210, primes) / 210
		#print 1.0 * phi(2310, primes) / 2310
		#print 1.0 * phi(30030, primes) / 30030
		#print 1.0 * phi(510510, primes) / 510510
		
		ret = 1
		for p in primes:
			if ret * p > 1000000:
				return ret
			ret *= p
