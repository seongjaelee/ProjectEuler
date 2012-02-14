import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 18
		question = 'Find the maximum sum travelling from the top of the triangle to the base.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		file = open('problem018.txt', 'r')
		lines = file.readlines()
		file.close()
		
		triangle = []
		for line in lines:
			line = line[:-1]
			triangle.append([int(s) for s in line.split(' ')])
		
		for i in xrange(len(triangle)-2, -1, -1):
			for j in xrange(len(triangle[i])):
				triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
				
		return triangle[0][0]