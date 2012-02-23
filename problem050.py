import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 50
		question = 'Which prime, below one-million, can be written as the sum of the most consecutive primes?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def f(limit):
			primes = utility.getPrimes(limit)
			length = 1
			ret = 0
			for i in xrange(len(primes)):
				for j in xrange(i + length, len(primes) - 1):
					s = sum(primes[i:j+1])
					if s >= limit:
						break
					if s < limit and utility.isPrime(s, primes):
						length = len(primes[i:j+1])
						ret = s
			return ret
		
		assert f(1000) == 953
		return f(1000000)
