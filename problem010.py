import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 10
		question = 'Calculate the sum of all the primes below two million.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		ret = 0
		primes = []
		p = 2
		while p <= 2000000:
			ret += p
			primes.append(p)
			p = findNextPrime(primes)	
		return ret
