import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 43
		question = 'Find the sum of all pandigital numbers with an unusual sub-string divisibility property.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def checkProperty(pre, length, divisor):
			if len(pre) == length:
				return (pre[-3] * 100 + pre[-2] * 10 + pre[-1]) % divisor == 0
			return True

		def enumerateValidCombinations(pre, list):
			if len(list) == 0:
				yield []
			elif len(list) == 10:
				for i in xrange(1, len(list)):
					for c in enumerateValidCombinations(pre + [list[i]], list[:i] + list[i+1:]):
						yield [i] + c
			else:
				for i in xrange(0, len(list)):
					ppre = pre + [list[i]]
					
					if not checkProperty(ppre, 4, 2):
						continue
					if not checkProperty(ppre, 5, 3):
						continue
					if not checkProperty(ppre, 6, 5):
						continue
					if not checkProperty(ppre, 7, 7):
						continue
					if not checkProperty(ppre, 8, 11):
						continue
					if not checkProperty(ppre, 9, 13):
						continue
					if not checkProperty(ppre, 10, 17):
						continue
					
					for c in enumerateValidCombinations(ppre, list[:i] + list[i+1:]):
						yield [list[i]] + c

		list = [i for i in xrange(10)]
		ret = 0
		for c in enumerateValidCombinations([], list):
			s = ''
			for i in c:
				s = s + str(i)
			ret += int(s)
		return ret