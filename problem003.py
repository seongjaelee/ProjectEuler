import problem
from utility import *
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 3
		question = 'Find the largest prime factor of a composite number.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		t = 600851475143
		primes = [2]
		while t > 1:
			while t % primes[-1] == 0:
				t /= primes[-1]
			if t != 1:
				primes.append(findNextPrime(primes))
		return primes[-1]


