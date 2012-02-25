import problem
import math
import utility
import sys

class Problem(problem.Problem):
	def __init__(self):
		number = 51
		question = 'Find the smallest prime which, by changing the same part of the number, can form eight different primes.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		
		n = 2
		while True:
			primes = [p for p in utility.getPrimes(pow(10, n))]
			
			for p in primes:
				if p < pow(10, n-1):
					continue
				
				for i in xrange(10):
					if str(p).count('%d' % (i)) == 0:
						continue
						
					count = 0
					for j in xrange(10):
						if int(str(p)[0]) == i and j == 0:
							continue
						q = int(str(p).replace('%d' % (i), '%d' % (j)))
						if p == q or utility.isPrime(q, primes):
							count += 1
					
					if count == 8:
						return p
			n += 1
