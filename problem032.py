import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 32
		question = 'Find the sum of all numbers that can be written as pandigital products.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def enumerateCombinations(list):
			if len(list) == 1:
				yield list
			else:
				for i in xrange(len(list)):
					for c in enumerateCombinations(list[:i] + list[i+1:]):
						yield [list[i]] + c
		
		l = [i for i in xrange(1, 10)]
		ret = set()
		for e in enumerateCombinations(l):
			a = e[0]*10 + e[1]
			b = e[2]*100 + e[3]*10 + e[4]
			c = e[5]*1000 + e[6]*100 + e[7]*10 + e[8]
			if a * b == c:
				ret.add(c)
			a = e[0]
			b = e[1]*1000 + e[2]*100 + e[3]*10 + e[4]
			c = e[5]*1000 + e[6]*100 + e[7]*10 + e[8]
			if a * b == c:
				ret.add(c)
		return sum(ret)