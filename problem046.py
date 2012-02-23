import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 46
		question = 'What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def findNextOddComposite(n, primes):
			m = n+2
			while True:
				primes = getPrimesFrom(m, primes)
				if not isPrime(m, primes):
					return m, primes
				m += 2
		
		n = 9
		primes = [2]
		while True:
			success = False
			for i in xrange(1, int(math.sqrt(0.5*n)) + 1):
				if isPrime(n - 2 * i * i, primes):
					success = True
					break
			if not success:
				return n
			n, primes = findNextOddComposite(n, primes)
			primes.append(n)