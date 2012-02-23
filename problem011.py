import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 11
		question = 'What is the greatest product of four adjacent numbers on the same straight line in the 20 by 20 grid?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		file = open('problem011.txt', 'r')
		lines = file.readlines()
		file.close()
		
		list = []
		for line in lines:
			list += [int(s) for s in line.split(' ')]
		
		ret = 0
		for i in xrange(len(list)):
			# horizontal
			if i / 20 == (i+3) / 20:
				ret = max(ret, list[i] * list[i+1] * list[i+2] * list[i+3])
			# vertical
			if i + 60 < len(list):
				ret = max(ret, list[i] * list[i+20] * list[i+40] * list[i+60])
			# diagonal a
			if i + 60 < len(list) and i / 20 == (i+3) / 20:
				ret = max(ret, list[i] * list[i+21] * list[i+42] * list[i+63])
			# diagonal b
			if i + 60 < len(list) and i / 20 == (i-3) / 20:
				ret = max(ret, list[i] * list[i+19] * list[i+38] * list[i+57])
		
		return ret