import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 15
		question = 'Starting in the top left corner in a 20 by 20 grid, how many routes are there to the bottom right corner?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def getNumPaths(x, y, n, cache = None):
			if cache == None:
				cache = [-1 for i in xrange(n*n)]
			if x == n or y == n:
				return 1
			index = x + y*n
			if cache[index] == -1:
				cache[index] = getNumPaths(x + 1, y, n, cache) + getNumPaths(x, y + 1, n, cache)
			return cache[index]
			
		assert 6 == getNumPaths(0, 0, 2)
		return getNumPaths(0, 0, 20)