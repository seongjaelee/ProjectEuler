import problem
import math
import sys
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 30
		question = ''
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def permute(arr):
			if len(arr) == 1:
				yield arr
			else:
				for i in xrange(len(arr)):
					subarr = arr[:i] + arr[i+1:]
					for p in permute(subarr):
						yield [arr[i]] + p
		
		def enumerateNumbers(arr):
			for p in permute(arr):
				ret = 0
				for i in xrange(len(p)):
					ret *= 10
					ret += p[i]
				yield ret
		
		def combinate(n, l):
			if l == 1:
				for i in xrange(n):
					yield [i]
			else:
				for i in xrange(n):
					for j in combinate(i+1, l-1):
						yield j + [i]
		
		def f(n, l):
			ret = 0
			for i in n:
				ret += pow(i, l)
			return ret
		
		def g(n, l):
			ret = 0
			for c in combinate(10, n):
				v = f(c, l)
				for e in enumerateNumbers(c):
					if e == v and v >= 2:
						ret += v
						print v
						break
			return ret
		
		return g(6, 5)