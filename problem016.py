import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 16
		question = 'What is the sum of the digits of the number 2^1000?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):

		numbers = [0 for i in xrange(int(math.log(2) * 1000.0 / math.log(10)) + 1)]
		numbers[0] = 1
		digit = 1

		for i in xrange(1000):
			for j in xrange(digit+1):
				numbers[j] *= 2
			for j in xrange(digit+1):
				if numbers[j] >= 10:
					numbers[j+1] += numbers[j] / 10
					numbers[j] = numbers[j] % 10
					if j == digit:
						digit += 1

		ret = 0
		for i in xrange(digit+1):
			ret += numbers[i]
		return ret			
