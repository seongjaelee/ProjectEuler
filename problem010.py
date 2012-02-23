import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 10
		question = 'Calculate the sum of all the primes below two million.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		return sum(getPrimes(2000000))
		