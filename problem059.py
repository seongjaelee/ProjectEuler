import problem
import math
import utility
import operator

class Problem(problem.Problem):
	def __init__(self):
		number = 59
		question = 'Using a brute force attack, can you decrypt the cipher using XOR encryption?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		file = open('problem059.txt', 'r')
		text = file.read()
		file.close()
		
		text = text.replace('\n', '')
		text = text.replace('\r', '')
		m = [int(t) for t in text.split(',')]
		
		def decrypt(message, keys):
			return [operator.xor(m, keys[i % len(keys)]) for i, m in enumerate(message)]
		
		def printMessage(message):
			ret = ''
			for m in message:
				ret += chr(m)
			return ret
		
		def enumerateKeys():
			for a in xrange(ord('a'), ord('z') + 1):
				for b in xrange(ord('a'), ord('z') + 1):
					for c in xrange(ord('a'), ord('z') + 1):
						yield [a, b, c]

		ret = 0
		maxVal = 0
		for key in enumerateKeys():
			d = decrypt(m, key)
			v = printMessage(d).count(' the ')
			if maxVal < v:
				ret += sum(d)
				maxVal = v
		return ret