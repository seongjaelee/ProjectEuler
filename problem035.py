import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 35
		question = 'How many circular primes are there below one million?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def getNumberOfDigits(n):
			ret = 0
			while n != 0:
				ret += 1
				n = n / 10
			return ret
			
		def getCircular(p):
			nDigits = getNumberOfDigits(p)
			for i in xrange(nDigits - 1):
				p = str(p)[1:] + str(p)[0]
				yield int(p)
		
		def isCircular(p, primes):
			if '0' in str(p):
				return False
			if p != 2 and '2' in str(p):
				return False
			if '4' in str(p):
				return False
			if '6' in str(p):
				return False
			if '8' in str(p):
				return False
			nDigits = getNumberOfDigits(p)
			for e in getCircular(p):
				if not isPrime(e, primes):
					return False
			return True
		
		def f(n):
			primes = getPrimes(n)
			ret = 0
			for p in primes:
				if isCircular(p, primes):
					ret += 1
			return ret
		
		assert f(100) == 13
		return f(1000000)