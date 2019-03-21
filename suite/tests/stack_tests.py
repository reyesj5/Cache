#!/usr/bin/env python
# coding=utf-8

import sys
import argparse
sys.path.insert(0, '../scripts')

from fibonacci import *
import time
import multiprocessing

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Testing the use of a stack with recursion and increasing fibonacci sequence.
def test1(n = 45, name = 'fib'):
	print('Stack Test 1')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'fibonacci number.'
		nth = fib(i)
		#print 'This fib took', time.time()-start, 'seconds.'

# Testing the use of a stack with recursion and fibonacci seqeunce multiple times (small) stack.
def test2(n = 50, ith = 40):
	print('Stack Test 2')
	for i in range(n):
		#Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		for j in range(ith):
			#start = time.time()
			#print 'Currently on the', j, 'iteration.'
			nth = fib(j)
			#print 'Iteration', j, 'took', time.time()-start, 'seconds.'
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing the use of a stack with recursion and fibonacci seqeunce multiple times (medium) stack.
def test3(n = 30, ith = 40):
	print('Stack Test 3')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		for j in range(ith,ith+2):
			nth = fib(j)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

tests = [test1,test2,test3]

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def worker(test = 1):
    #worker function
    try:
    	tests[test-1]()
    except:
    	raise ValueError("Test not implemented")


# Using multiprocessing to ensure all cores in the system are being used/tested
def test(n = 1, cores = multiprocessing.cpu_count()):
	# Measuring how long a script runs
	start = time.time()
	jobs = []
	for i in range(cores):
		p = multiprocessing.Process(target=worker, args=(n,))
		jobs.append(p)
		p.start()
	while True:
	    if any(proces.is_alive() for proces in jobs):
	        time.sleep(1)
	    else:
	        print('All processes done')
	        print 'Script took', time.time()-start, 'seconds.'
	        break

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--test", type=int, help="Which test to run, default t=1")
	parser.add_argument("-c", "--cores", type=int, help="The number of cores to use, default c=Number of available CPUs in architecture")
	args = parser.parse_args()
	n_test = 1
	cores = multiprocessing.cpu_count()
	if not(args.test == None):
		n_test = args.test
	if not(args.cores == None):
		cores = args.cores
	test(n_test, cores)