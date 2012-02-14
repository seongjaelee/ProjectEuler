import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 6
		question = 'What is the difference between the sum of the squares and the square of the sums?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		n = 100
		return n * n * (n+1) * (n+1) / 4 - n * (n+1) * (2*n+1) / 6
