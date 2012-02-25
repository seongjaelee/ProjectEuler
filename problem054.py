import problem
import math
import utility

class Problem(problem.Problem):
	def __init__(self):
		number = 54
		question = 'How many hands did player one win in the game of poker?'
		problem.Problem.__init__(self, number, question)

	def getAnswer(self):
		def isSameSuit(hands):
			s = hands[0][1]
			for h in hands:
				if h[1] != s:
					return False
			return True
		
		def isStraightStartingFrom(hands, i):
			l = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
			#assert i < len(l) - 4
			for j in xrange(0, 5):
				check = False
				for h in hands:
					if l[i + j] == h[0]:
						check = True
				if not check:
					return False
			return True
		
		def isStraight(hands):
			l = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
			for i in xrange(len(l) - 4):
				if isStraightStartingFrom(hands, i):
					return True, i + 2 + 4
			return False, None
		
		def matchNumbers(hands):
			l = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
			ret = [0 for i in l]
			for i in xrange(len(l)):
				for h in hands:
					if h[0] == l[i]:
						ret[i] += 1
			#assert sum(ret) == 5
			return ret
		
		def getSortedScore(matches, n, expectedLength):
			ret = []
			for i, m in enumerate(matches):
				if m == n:
					ret.append(i+2)
			ret = sorted(ret)
			ret.reverse()
			#assert len(ret) == expectedLength
			#for i in xrange(len(ret)-1):
			#	assert ret[i] > ret[i+1]
			return ret
		
		def getScore(hands):
			matches = matchNumbers(hands)
			straightInfo = isStraight(hands)
			flushInfo = isSameSuit(hands)
			fourMatch = matches.count(4)
			threeMatch = matches.count(3)
			twoMatch = matches.count(2)
			
			# Royal Flush and Straight Flush
			if straightInfo[0] and flushInfo:
				return [8, straightInfo[1]]
			# Four of a Kind
			elif fourMatch == 1:
				return [7] + getSortedScore(matches, 4, 1)
			# Full house
			elif twoMatch == 1 and threeMatch == 1:
				return [6] + getSortedScore(matches, 3, 1)
			# Flush
			elif flushInfo:
				return [5] + getSortedScore(matches, 1, 5)
			# Straight
			elif straightInfo[0]:
				return [4, straightInfo[1]]
			# Three of a Kind
			elif threeMatch == 1:
				return [3] + getSortedScore(matches, 3, 1)
			# Two Pairs
			elif twoMatch == 2:
				return [2] + getSortedScore(matches, 2, 2) + getSortedScore(matches, 1, 1)
			# One Pair
			elif twoMatch == 1:
				return [1] + getSortedScore(matches, 2, 1) + getSortedScore(matches, 1, 3)
			# High Card
			else:
				return [0] + getSortedScore(matches, 1, 5)
		
		def poker(a, b):
			#assert len(a) == len(b)
			sa = getScore(a)
			sb = getScore(b)
			
			if sa[0] == sb[0]:
				#assert len(sa) == len(sb)
				for i in xrange(1, len(sa)):
					if sa[i] != sb[i]:
						return sa[i] > sb[i]
			
			#assert sa[0] != sb[0]
			return sa[0] > sb[0]
		
		def pokerFromLine(line):
			line = line.replace('\n', '')
			line = line.replace('\r', '')
			cards = line.split(' ')
			assert len(cards) == 10
			return poker(cards[:5], cards[5:])
			
		assert pokerFromLine('5H 5C 6S 7S KD 2C 3S 8S 8D TD') == False
		assert pokerFromLine('5D 8C 9S JS AC 2C 5C 7D 8S QH') == True
		assert pokerFromLine('2D 9C AS AH AC 3D 6D 7D TD QD') == False
		assert pokerFromLine('4D 6S 9H QH QC 3D 6D 7H QD QS') == True
		assert pokerFromLine('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D') == True
		
		file = open('problem054.txt', 'r')
		lines = file.readlines()
		file.close()
		
		assert len(lines) == 1000
		
		ret = 0		
		for line in lines:
			if pokerFromLine(line):
				ret += 1
		return ret