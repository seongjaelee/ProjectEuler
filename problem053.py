import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 53
		question = 'How many values of C(n,r), for 1 <= n <= 100, exceed one-million?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		
		logs = [math.log(i) for i in xrange(1, 101)]
		
		# nCr = n! / r!(n-r)! > 10^6
		# log nCr = sum_n log i - sum_r log i - sum_(n-r) log i > 6 log 10
		
		ret = 0
		for n in xrange(1, 101):
			for r in xrange(1, n):
				v = sum([logs[i-1] for i in xrange(r+1, n+1)]) - sum([logs[i-1] for i in xrange(1, n-r+1)])
				if v > 6.0 * logs[10-1]:
					ret += 1
		return ret