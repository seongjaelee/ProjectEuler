import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 2
		question = 'By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		ret = 0
		pair = (1, 1)
		while (True):
			pair = (pair[1], pair[0] + pair[1])
			if pair[0] % 2 == 0:
				ret += pair[0]
			if pair[0] >= 4000000:
				break
		return ret
