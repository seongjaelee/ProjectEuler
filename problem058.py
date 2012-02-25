import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 58
		question = 'Investigate the number of primes that lie on the diagonals of the spiral grid.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
	
		primeLimit = 10000
		primes = utility.getPrimes(primeLimit)
		
		i = 0
		n = 1
		numPrime = 0
		numTotal = 1
		while True:
			i += 1
			
			for j in xrange(4):
				n = n + 2 * i
				
				if n >= primeLimit * primeLimit:
					primeLimit *= 2
					primes = utility.getPrimes(primeLimit)
					
				if utility.isPrime(n, primes):
					numPrime += 1
				numTotal += 1
			
			if numTotal > numPrime * 10:
				return i * 2 + 1