import math

def isPrime(number, primes):
	if number == 1:
		return False
	for p in primes:
		if p * p > number:
			return True
		if number % p == 0:
			return False
	return True

def findNextPrime(primes):
	i = primes[-1] + 1
	while True:
		if isPrime(i, primes):
			return i
		i += 1

def getPrimesFrom(limit, primes):
	p = 2
	if len(primes) != 0:
		p = primes[-1]
	if p > limit:
		return primes

	while True:
		p = findNextPrime(primes)
		if p > limit:
			break
		primes.append(p)
	
	return primes

def getPrimes(limit):
	return getPrimesFrom(limit, [2])

def factorize(n, primes):
	if isPrime(n, primes):
		return ([n], [1])

	ret = ([], [])
	for p in primes:
		m = n
		if m % p == 0:
			ret[0].append(p)
			ret[1].append(0)
			while m % p == 0:
				m /= p
				ret[1][-1] += 1
	return ret
		
def getDivisors(n):
	ret = []
	for i in xrange(1, int(math.sqrt(n) + 1)):
		if n % i == 0:
			ret.append(i)
			if i*i != n:
				ret.append(n/i)
	return ret

def getDivisors2(n, primes):
	def enumerateFactors(factors):
		ret = [0 for i in factors[1]]
		isDone = False
		while not isDone:
			yield ret
			for i, f in enumerate(factors[1]):
				if ret[i] == f:
					ret[i] = 0
					if i == len(factors[1]) - 1:
						isDone = True
				else:
					ret[i] += 1
					break
	
	factors = factorize(n, primes)
	ret = []
	for subFactors in enumerateFactors(factors):
		r = 1
		for i, j in zip(factors[0], subFactors):
			r *= pow(i, j)
		ret.append(r)
	return ret