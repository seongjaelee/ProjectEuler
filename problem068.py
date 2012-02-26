import problem
import math
import utility
import itertools
from math import sqrt
from math import floor

class Problem(problem.Problem):
	def __init__(self):
		number = 68
		question = 'What is the maximum 16-digit string for a "magic" 5-gon ring?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def f(p):
			#     5
			#       1    9
			#    2    0
			# 6   3--4---8
			#      7
			
			assert len(p) == 9
			
			l = [(p[5], p[1], p[0]), (10, p[0], p[4]), (p[8], p[4], p[3]), (p[7], p[3], p[2]), (p[6], p[2], p[1])]
			
			minArg, minVal = 0, l[0][0]
			for i in xrange(1, 5):
				if minVal > l[i][0]:
					minArg, minVal = i, l[i][0]
			
			r = []
			for i in xrange(0, 5):
				j = minArg + i - 5
				if j >= 5:
					j -= 5
				r.append(l[j])
			
			ret = ''
			for i in r:
				ret += str(i[0]) + str(i[1]) + str(i[2])
			return int(ret)
			
		maxVal = 0
		for p in itertools.permutations(range(1, 10)):
			a = p[0] + p[1] + p[5]
			if a != p[1] + p[2] + p[6]:
				continue
			if a != p[2] + p[3] + p[7]:
				continue
			if a != p[3] + p[4] + p[8]:
				continue
			if a != p[4] + p[0] + 10:
				continue
			print f(p)
			maxVal = max(maxVal, f(p))
		return maxVal