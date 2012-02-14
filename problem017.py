import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 17
		question = 'How many letters would be needed to write all the numbers in words from 1 to 1000?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		a = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
		b = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
		c = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
		
		# [1, 99]
		# a is used in 9 times 0x 2x 3x 4x 5x 6x 7x 8x 9x
		# b is used in 1 times 1x
		# c is used 10 times
		d = sum([len(s) for s in a]) * 9 + sum([len(s) for s in b]) + sum([len(s) for s in c]) * 10
		
		return len('hundredand') * 900 + sum([len(s) for s in a]) * 100 + d * 10 + len('onethousand') - len('and')*9