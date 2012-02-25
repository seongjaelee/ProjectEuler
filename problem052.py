import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 52
		question = 'Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits in some order.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		
		def containSameDigits(a, b):
			sa = str(a)
			sb = str(b)
			if len(sa) != len(sb):
				return False
			for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
				if sa.count(i) != sb.count(i):
					return False
			return True

		n = 1		
		while True:
			if containSameDigits(n, 2*n):
				if containSameDigits(n, 3*n):
					if containSameDigits(n, 4*n):
						if containSameDigits(n, 5*n):
							if containSameDigits(n, 6*n):
								return n
			n += 1