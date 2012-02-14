import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 20
		question = 'Find the sum of digits in the number 100!'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):

		t = 0.0
		for i in xrange(1, 101):
			t += math.log(i)
		t /= math.log(10)
		
		numbers = [0 for i in xrange(int(t) + 1)]
		numbers[0] = 1
		nDigits = 1

		for i in xrange(100):
			for j in xrange(nDigits):
				numbers[j] *= (i+1)
			for j in xrange(nDigits):
				if numbers[j] >= 10:
					numbers[j+1] += numbers[j] / 10
					numbers[j] = numbers[j] % 10
			for j in xrange(nDigits, len(numbers)):
				if numbers[j] == 0:
					break
				nDigits += 1
				if numbers[j] >= 10:
					numbers[j+1] += numbers[j] / 10
					numbers[j] = numbers[j] % 10

		ret = 0
		for i in xrange(nDigits):
			ret += numbers[i]
		return ret		
