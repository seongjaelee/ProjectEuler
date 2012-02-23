import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 47
		question = 'Find the first four consecutive integers to have four distinct primes factors.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def hasOnlyNFactors(i, n, primes):
			nFactors = 0
			for p in primes:
				if i % p == 0:
					nFactors += 1
					i /= p
					while i % p == 0:
						i /= p

				if nFactors == n:
					return i == 1
				if i == 1:
					return False
				if pow(p, n-nFactors) > i:
					return False
			return False
		
		def f(n):
			i = 2
			primes = [2]
			validCount = 0
			while True:
				i += 1
				# we don't care about when i is a prime, so primes until i/2 is okay.
				if primes[-1] < i/2:
					primes = utility.getPrimesFrom(i/2 + 10000, primes)
				if hasOnlyNFactors(i, n, primes):
					if validCount == n-1:
						return i-n+1
					else:
						validCount += 1
				else:
					validCount = 0
		
		assert f(2) == 14
		assert f(3) == 644
		return f(4)