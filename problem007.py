import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 7
		question = 'Find the 10001st prime.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		primes = [2]
		i = 1
		while i != 10001:
			primes.append(findNextPrime(primes))
			i += 1
		return primes[-1]
