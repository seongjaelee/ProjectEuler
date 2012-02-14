import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 5
		question = 'What is the smallest number divisible by each of the numbers 1 to 20?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		number = 20
		primes = getPrimes(number)	
		ret = 1
		for p in primes:
			ret *= pow(p, int(math.floor(math.log(number) / math.log(p))))
		return ret
