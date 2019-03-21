#!/usr/bin/env python
# coding=utf-8

import sys
import argparse
sys.path.insert(0, '../scripts')

from matrices import *
import time
import multiprocessing

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Testing random matrix of ~4000 elements multiplied by another random matrix 80000 times.
def test1(n = 80000, size = 63):
	print('Matrices Test 1')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		matrix1 = random_matrix(size,size)
		matrix2 = random_matrix(size,size)
		mult_matrix(matrix1, matrix2)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random matrix of ~4000 elements multiplied by itself 80000 times.
def test2(n = 80000, size = 63):
	print('Matrices Test 2')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		matrix1 = random_matrix(size,size)
		mult_matrix(matrix1, matrix1)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random matrix of ~4000 elements multiplied by another random matrix 80000 times.
def test3(n = 80000, size = 63):
	print('Matrices Test 3')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		matrix1 = random_matrix(size,size)
		matrix2 = identity_matrix(size)
		mult_matrix(matrix1, matrix2)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random matrix of ~ 4000 elements sumed to another random matrix 320000 times.
def test4(n = 320000, size = 63):
	print('Matrices Test 4')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		matrix1 = random_matrix(size,size)
		matrix2 = random_matrix(size,size)
		sum_matrix(matrix1, matrix2)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random matrix of ~ 4000 elements sumed to another random matrix 600000 times.
def test5(n = 600000, size = 63):
	print('Matrices Test 5')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		matrix1 = random_matrix(size,size)
		sum_matrix(matrix1, matrix1)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random matrix of 1000x1000 elements transposed 15000 times.
def test6(n = 15000, size = 1000):
	print('Matrices Test 6')
	matrix = random_matrix(size,size)
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		matrix = transpose(matrix)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random matrix of 1000x1000 elements transposed 18000 times.
def test6(n = 18000, size = 1000):
	print('Matrices Test 6')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		matrix = random_matrix(size,size)
		matrix = transpose(matrix)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

# Testing random matrix of 1000000 elements converted to list 24000 times
def test7(n = 24000, size = 1000):
	print('Matrices Test 7')
	for i in range(n):
		# Measuring how long a script runs
		#start = time.time()
		#print 'Currently on the', i, 'iteration.'
		matrix = random_matrix(size,size)
		matrix2list(matrix)
		#print 'Iteration', i, 'took', time.time()-start, 'seconds.'

tests = [test1,test2,test3,test4,test5,test6,test7]

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