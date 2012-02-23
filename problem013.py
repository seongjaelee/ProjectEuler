import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 13
		question = 'Find the first ten digits of the sum of one-hundred 50-digit numbers.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		file = open('problem013.txt', 'r')
		lines = file.readlines()
		file.close()
		
		list = []
		for line in lines:
			if line[-1] == '\r' or line[-1] == '\n':
				line = line[:-1]
			list.append([int(s) for s in line])
		assert len(list) == 100
		
		for i in xrange(len(list)):
			list[i].reverse()
			
		ret = [0 for i in xrange(52)]
		for i in xrange(50):
			ret[i] += sum([l[i] for l in list])
			ret[i+1] += ret[i] / 10
			ret[i] %= 10
			
		ret[50] += ret[49] / 10
		ret[49] %= 10
		ret[51] += ret[50] / 10
		ret[50] %= 10
		ret.reverse()
		
		s = ''
		for i in xrange(10):
			s += str(ret[i])
		return int(s)