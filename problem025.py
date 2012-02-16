import problem
import math
import sys

class Problem(problem.Problem):
	def __init__(self):
		number = 25
		question = 'What is the first term in the Fibonacci sequence to contain 1000 digits?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		
		bucketDigits = int(math.log(sys.maxint) / math.log(10)) + 1 - 1
		bucketSize = pow(10, bucketDigits)
	
		def sum(a, b):
			size = max(len(a), len(b))
			ret = [0 for i in xrange(size)]
			for i in xrange(size):
				if i < len(a) and i < len(b):
					ret[i] = a[i] + b[i]
				elif i < len(a):
					ret[i] = a[i]
				elif i < len(b):
					ret[i] = b[i]
			for i in xrange(size - 1):
				if ret[i] >= bucketSize:
					ret[i] -= bucketSize
					ret[i+1] += 1
			if ret[-1] >= bucketSize:
				ret[-1] -= bucketSize
				ret.append(1)
			return ret
		
		def nDigits(n):
			for i in xrange(len(n) - 1, -1, -1):
				if n[i] != 0:
					ret = 0
					m = n[i]
					while m != 0:
						m /= 10
						ret += 1
					return i * bucketDigits + ret
		
		assert nDigits([200]) == 3
		assert nDigits([1, 20]) == bucketDigits + 2
		
		def getFibonacciIndex(digits):
			ret = 1
			a = [1]
			b = [1]
			while nDigits(a) < digits:
				c = sum(a, b)
				a = b
				b = c
				ret += 1
			return ret
		
		assert getFibonacciIndex(2) == 7
		assert getFibonacciIndex(3) == 12
		return getFibonacciIndex(1000)