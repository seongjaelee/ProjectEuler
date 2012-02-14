import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 67
		question = 'Using an efficient algorithm find the maximal sum in the triangle?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		# Copied from problem018.py
		file = open('problem067.txt', 'r')
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