import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 9
		question = 'Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		#     a*a + b*b = (1000-a-b)^2
		# <=> 1000(a+b) = 500000 + ab
		for a in xrange(1, 334):
			for b in xrange(a+1, (1000-a)/2 + 1):
				if 1000 * (a + b) == 500000 + a * b:
					return a * b * (1000 - a - b)
				
