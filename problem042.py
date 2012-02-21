import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 42
		question = 'How many triangle words does the list of common English words contain?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		triangles = [1]
		
		def updateTriangles(limit):
			while limit > triangles[-1]:
				n = len(triangles) + 1
				triangles.append(n * (n+1) / 2)
		
		def convert(word):
			ret = 0
			for w in word:
				ret += ord(w) - ord('A') + 1
			return ret
		
		updateTriangles(convert('SKY'))
		assert convert('SKY') in triangles
		
		file = open('problem042.txt', 'r')
		text = file.read()
		file.close()
		
		text = text[1:-1]
		words = text.split('","')

		ret = 0
		for word in words:
			n = convert(word)
			updateTriangles(n)
			if n in triangles:
				ret += 1
		return ret