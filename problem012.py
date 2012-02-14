import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 12
		question = 'What is the value of the first triangle number to have over five hundred divisors?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):

		def getNumberOfDivisors(n, primes):
			ret = 1
			for p in primes:
				t = 1
				while n % p == 0:
					n /= p
					t += 1
				ret *= t
				if n == 1:
					break
			return ret

		n = 2
		primes = [2]
		prevNumberOfDivisors = 2
		nextNumberOfDivisors = 1
		while (True):
			while primes[-1] < n+1:
				primes.append(findNextPrime(primes))
			
			if n % 2 == 0:
				nextNumberOfDivisors = getNumberOfDivisors(n+1, primes)
			else:
				nextNumberOfDivisors = getNumberOfDivisors((n+1)/2, primes)
			
			# n and n+1 doesn't share any common divisors.
			m = prevNumberOfDivisors * nextNumberOfDivisors
			if m > 500:
				return n*(n+1)/2
			
			prevNumberOfDivisors = nextNumberOfDivisors
			n += 1
