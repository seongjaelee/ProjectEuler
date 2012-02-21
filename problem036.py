import problem
import math
from utility import *

class Problem(problem.Problem):
	def __init__(self):
		number = 36
	 	question = 'Find the sum of all numbers less than one million, which are palindromic in base 10 and base 2.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def isPalindrome(n):
			s = str(n)
			l = len(s)
			for i in xrange((l + 1) / 2):
				if s[i] != s[l-1-i]:
					return False
			return True
			
		def convertBinary(n):
			ret = ''
			while n != 0:
				ret = str(n % 2) + ret
				n /= 2
			return ret
		
		ret = 0
		for i in xrange(1, 1000000):
			if isPalindrome(i) and isPalindrome(convertBinary(i)):
				ret += i
		return ret