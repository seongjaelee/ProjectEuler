import problem
import math
import sys
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 27
		question = 'Find a quadratic formula that produces the maximum number of primes for consecutive values of n'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def f(a, b, primes):
			n = 0
			while True:
				v = n * n + a * n + b
				if v <= 0:
					break
				primes = getPrimes2(v, primes)
				if isPrime(v, primes):
					n += 1
				else:
					break
			return n
		
		primes = [2]
		assert f(1, 41, primes) == 40
		assert f(-79, 1601, primes) == 80
		
		maxValue = 40
		ret = 41
		for a in xrange(-999, 1000, 1):
			for b in xrange(2, 1000):
				v = f(a, b, primes)
				if maxValue < v:
					maxValue = v
					ret = a * b
		return ret