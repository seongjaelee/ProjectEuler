#! /usr/bin/python
import glob
import time
import sys
import os
import problem
import utility

def isNumber(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def execute(problem):
	tic = time.clock()
	answer = p.getAnswer()
	toc = time.clock()
	
	print 'Problem %d' % (p.number)
	print '	%s' % (p.question)
	print '	%s' % (answer)
	print '	Took %f seconds' % (toc - tic)
	print ''	

if len(sys.argv) == 2 and isNumber(sys.argv[1]):
	i = int(sys.argv[1])
	if os.path.exists('problem%03d.py' % (i)):
		p = __import__('problem%03d' % (i)).Problem()
		execute(p)
	exit(0)

for filename in glob.glob('problem???.py'):
	p = __import__(filename[:-3]).Problem()
	execute(p)
