import problem
import math

class Problem(problem.Problem):
	def __init__(self):
		number = 55
		question = 'How many Lychrel numbers are there below ten-thousand?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def addReverse(a):
			b = a[::-1]
			carry = 0
			ret = ''
			for i in xrange(len(a)):
				c = int(a[i]) + int(b[i]) + carry
				carry = 0
				ret = ret + str(c % 10)
				if c >= 10:
					carry = 1
			if carry == 1:
				ret += '1'
			return ret[::-1]
		
		def isPalindromic(a):
			for i in xrange(len(a) / 2):
				if a[i] != a[len(a)-1-i]:
					return False
			return True
		
		def isLychrel(a):
			for i in xrange(50):
				a = addReverse(a)
				if isPalindromic(a):
					return False
			return True
		
		assert isLychrel('196')
		assert isLychrel('10677')
		
		a = '10677'
		for i in xrange(53):
			assert not isPalindromic(a)
			a = addReverse(a)
		assert isPalindromic(a)
		
		ret = 0
		for i in xrange(1, 10000):
			a = str(i)
			if isLychrel(a):
				ret += 1
		return ret