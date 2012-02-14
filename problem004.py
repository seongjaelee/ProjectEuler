import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 4
		question = 'Find the largest palindrome made from the product of two 3-digit numbers.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def isPalindrome(number):
			s = '%d' % (number)
			digits = len(s)
			for i in xrange(digits / 2):
				if s[i] != s[digits-i-1]:
					return False
			return True

		ret = 1
		for i in xrange(999, 99, -1):
			for j in xrange(999, i, -1):
				prod = i * j
				if prod < ret:
					continue
				if isPalindrome(prod):
					ret = prod
					continue

		return ret

