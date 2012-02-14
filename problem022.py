import problem
from utility import *
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 22
		question = 'What is the total of all the name scores in the file of first names?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		file = open('problem022.txt', 'r')
		text = file.read()
		file.close()
		
		text = text[1:]
		text = text[:-1]
		list = text.split('","')
		
		assert list[0] == 'MARY'
		assert list[-1] == 'ALONSO'
		
		def evaluate(name):
			ret = 0
			for n in name:
				ret += ord(n) - ord('A') + 1
			return ret
		
		assert evaluate('COLIN') == 53
		
		ret = 0
		for i, name in enumerate(sorted(list)):
			if i == 937:
				assert name == 'COLIN'
				assert (i+1) * evaluate(name) == 49714
			ret += (i+1) * evaluate(name)
		return ret