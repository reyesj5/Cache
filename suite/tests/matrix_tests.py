#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.insert(0, '../scripts')

from matrices import *

# Testing random matrix of ~4000 elements multiplied by another random matrix 4000 times.
def test1():
	n = 4000
	m = 63
	for i in range(n):
		matrix1 = random_matrix(m,m)
		matrix2 = random_matrix(m,m)
		mult_matrix(matrix1, matrix2)

# Testing random matrix of 1000x1000 elements transposed 4000 times.
def test2():
	n = 1000
	matrix = random_matrix(n,n)
	for i in range(4*n):
		matrix = transpose(matrix)

# Testing random matrix of ~ 4000 elements sumed to another random matrix 4000 times.
def test3():
	n = 4000
	m = 63
	for i in range(n):
		matrix1 = random_matrix(m,m)
		matrix2 = random_matrix(m,m)
		sum_matrix(matrix1, matrix2)

# Testing random matrix of 1000000 elements converted to list 4000 times
def test4():
	n = 1000
	for i in range(4*n):
		matrix = random_matrix(n,n)
		matrix2list(matrix)