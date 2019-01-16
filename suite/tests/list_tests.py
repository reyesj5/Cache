#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.insert(0, '../scripts')

from lists import *
import time
import multiprocessing

args = sys.argv

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Testing random list of 4000 elements multiplied by another random list 900000 times.
def test1(n = 900000, size = 4000):
	print('Lists Test 1')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		list1 = random_list(size)
		list2 = random_list(size)
		mult_lists(list1, list2)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random list of 4000 elements multiplied by itself 1250000 times.
def test2(n = 1250000, size = 4000):
	print('Lists Test 2')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		list1 = random_list(size)
		mult_lists(list1, list1)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random list of 100 elements expanded by iteself 1200 times.
def test3(n = 1200):
	print('Lists Test 3')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		list1 = random_list(100)
		list1 = expandByN(list1, 20)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random list of 4000 elements sumed to another random list 900000 times.
def test4(n = 900000, size = 4000):
	print('Lists Test 4')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		list1 = random_list(size)
		list2 = random_list(size)
		sum_lists(list1, list2)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random list of 4000 elements sumed to itself 1250000 times.
def test5(n = 1250000, size = 4000):
	print('Lists Test 5')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		list1 = random_list(size)
		sum_lists(list1, list1)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random list of 4000 elements converted to matrix 1250000 times
def test6(n = 1250000, size = 4000):
	print('Lists Test 6')
	for i in range(4000):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		list = random_list(size)
		list2matrix(list)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def worker(test = 1):
    #worker function
    tests = [test1,test2,test3,test4,test5,test6]
    try:
    	tests[test-1]()
    except:
    	raise ValueError("Test not implemented or ran out of memory!")

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
	if len(args) == 1:
		test()
	else:
		test(int(args[1]), int(args[2]))