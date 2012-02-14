import problem

class Problem(problem.Problem):
	def __init__(self):
		number = 14
		question = 'Find the longest sequence using a starting number under one million'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		
		nChains = [0 for i in xrange(10000000)]
		nChains[1] = 1

		def getNextSequence(n):
			assert n > 1
			if n % 2 == 0:
				return n / 2
			else:
				return n * 3 + 1

		def getNumChains(n):
			if n == 1:
				return 1

			m = getNextSequence(n)
			if m >= len(nChains):
				return 1 + getNumChains(m)
			else:
				updateChains(m)
				return 1 + nChains[m]	

		def updateChains(n):
			if nChains[n] != 0:
				return

			m = getNextSequence(n)
			nChains[n] = 1 + getNumChains(m)

		for i in xrange(1, 1000000):
			updateChains(i)

		nChainsMax = 1
		ret = 1
		for i in xrange(1, 1000000):
			if nChains[i] > nChainsMax:
				ret = i
				nChainsMax = nChains[i]
		return ret	
