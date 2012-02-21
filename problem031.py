import problem
import math
import sys
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 31
		question = 'Investigating combinations of English currency denominations.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def getCombinations(coins, amount):
			if len(coins) == 1:
				if amount % coins[0] == 0:
					return 1
				else:
					return 0
			
			ret = 0
			for i in xrange(amount / coins[0] + 1):
				if coins[0] * i > amount:
					continue
				ret += getCombinations(coins[1:], amount - coins[0] * i)
			return ret
			
		coins = [200, 100, 50, 20, 10, 5, 2, 1]
		return getCombinations(coins, 200)