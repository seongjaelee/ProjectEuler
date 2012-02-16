import problem
from utility import *
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 24
		question = ''
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
	
		def getNth(n, nCandidates):
			n = n-1
			ret = []
			candidates = [i for i in xrange(nCandidates)]
			for i in xrange(nCandidates-1, -1, -1):
				j = n / math.factorial(i)
				n = n % math.factorial(i)
				ret.append(candidates[j])
				candidates.remove(candidates[j])
			for i in xrange(len(ret)):
				ret[i] = str(ret[i])
			return ''.join(ret)
			
		assert getNth(3, 3) == '102'
		
		return getNth(1000000, 10)
