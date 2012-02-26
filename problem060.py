import problem
import math
import utility
import itertools
import sys

class Problem(problem.Problem):
	def __init__(self):
		number = 60
		question = 'Find a set of five primes for which any two primes concatenate to produce another prime.'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
	
		limit = 27000
		primes = utility.getPrimes(limit)
		
		def isConcatenatedPrime(p, q, primes):
			return utility.isPrime(int(p + q), primes) and utility.isPrime(int(q + p), primes)

		graph = [[] for i in xrange(len(primes))]
		strPrimes = [str(p) for p in primes]
		for i in xrange(len(primes)):
			for j in xrange(i+1, len(primes)):
				if isConcatenatedPrime(strPrimes[i], strPrimes[j], primes):
					graph[i].append(j)
					graph[j].append(i)
		
		# we need a n-complete subgraph inside the graph
		def findCompleteGraphs(graph, n):
			if n == 3:
				for i in xrange(len(primes)):
					for j in graph[i]:
						if j < i:
							continue
						for k in graph[j]:
							if k < j:
								continue
							if k in graph[i]:
								yield [i, j, k]
			else:
				for g in findCompleteGraphs(graph, n-1):
					for k in graph[g[-1]]:
						if k < g[-1]:
							continue
						isComplete = True
						for gi in g:
							if gi not in graph[k]:
								isComplete = False
								break
						if isComplete:
							yield g + [k]
		
		ret = sys.maxint
		for c in findCompleteGraphs(graph, 5):
			ret = max(ret, sum(primes[i] for i in c))
				
		assert primes[-1] > ret
		return ret