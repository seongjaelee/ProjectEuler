import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 41
		question = 'What is the largest n-digit pandigital prime that exists?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		primes = utility.getPrimes(int(math.sqrt(987654321)) + 1)
		def isPrime(n):
			return utility.isPrime(n, primes)
	
		def enumerateCombinations(n, useEven):
			if len(n) == 1:
				yield n
			
			for i in xrange(len(n)):
				if not useEven and n[i] % 2 == 0:
					continue
				for c in enumerateCombinations(n[:i] + n[i+1:], True):
					yield c + [n[i]]
		
		def getPandigitalPrimes(nDigits):
			digits = [i+1 for i in xrange(nDigits)]
			for c in enumerateCombinations(digits, False):
				p = 0
				for i in c:
					p *= 10
					p += i
				if isPrime(p):
					yield p
		
		ret = 0
		for i in xrange(9, -1, -1):
			for p in getPandigitalPrimes(i):
				if ret < p:
					ret = p
			if ret != 0:
				break
		return ret