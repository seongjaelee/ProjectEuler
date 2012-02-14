import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 1
		question = 'Add all the natural numbers below one thousand that are multiples of 3 or 5.'
		problem.Problem.__init__(self, number, question)
	
	def getAnswer(self):
		ret = 0
		for i in xrange(1, 1000):
			if i % 3 == 0 or i % 5 == 0:
				ret += i
		return ret
