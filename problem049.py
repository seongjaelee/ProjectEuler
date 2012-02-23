import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 49
		question = 'Find arithmetic sequences, made of prime terms, whose four digits are permutations of each other.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def isPermutations(p, q, r):
			p = str(p)
			q = str(q)
			r = str(r)
			for i in xrange(10):
				s = '%d' % i
				if p.count(s) != q.count(s) or q.count(s) != r.count(s):
					return False
			return True
		
		primes = utility.getPrimes(10000)
		for i in xrange(len(primes)):
			if primes[i] < 1000:
				continue
			for j in xrange(i + 1, len(primes)):
				p = primes[i]
				q = primes[j]
				r = q + q - p
				if r > 10000 or not utility.isPrime(r, primes):
					continue
				if not isPermutations(p, q, r):
					continue
				if p == 1487:
					continue
				return int(str(p) + str(q) + str(r))
		return -1