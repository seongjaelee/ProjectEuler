import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 34
		question = 'Find the sum of all numbers which are equal to the sum of the factorial of their digits.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		facts = [math.factorial(i) for i in xrange(1, 10)]
		
		def enumerateCombinations(n, max):
			if n == 1:
				for i in xrange(max, -1, -1):
					yield [i]
			else:
				for i in xrange(max, -1, -1):
					for c in enumerateCombinations(n-1, i):
						yield [i] + c
		
		def getSumOfFactorials(c):
			ret = 0
			for i in c:
				ret += math.factorial(i)
			return ret
		
		def getDigits(n):
			ret = []
			while n != 0:
				ret.append(n % 10)
				n = n / 10
			return ret
		
		def isCurious(c, s):
			digits = getDigits(s)
			for i in xrange(0, 10):
				if digits.count(i) != c.count(i):
					return False
			return True
		
		# 7 * 9! = 2540160. We cannot have more than 7 digits
		ret = 0
		for nDigits in xrange(2, 8):
			for c in enumerateCombinations(nDigits, 9):
				s = getSumOfFactorials(c)
				if isCurious(c, s):
					ret += s
		return ret