#!/usr/bin/env python
# coding=utf-8
import random

# Creates a matrix WxL filled with 0's
def empty_matrix(w, l):
	result = []
	# iterate through rows
	for i in range(w):
		row = []
		# iterate through columns 
		for j in range(l):
			row.append(0.0)
		result.append(row)
	return result

# returns the nxn identity matrix 
def identity(n):
	result = []
	r, c = 0.0, 0.0
	# iterate through rows
	for i in range(n):
		row = []
		# iterate through columns 
		for j in range(n):
			if (i==r) and (j==c):
				row.append(1.0)
				r += 1
				c += 1
			else:
				row.append(0.0)
		result.append(row)
	return result

# returns a matrix WxL of random values
def random_matrix(w, l):
	result = []
	# iterate through rows
	for i in range(w):
		row = []
		# iterate through columns 
		for j in range(l):
			row.append(random.randint(0,4000))
		result.append(row)
	return result

# multiplies two matrices by each other
def mult_matrix(a,b):
	# Checks if matrices can be multiplied: m×n by n×p = m×p
	if len(a[0]) != len(b):
		raise ValueError("Matrices with these dimensions cannot be multiplied.")
	# store result in a new matrix
	result = []
	# iterate through rows of a
	for i in range(len(a)):
		# new list to store new row values
		row = []
		# iterate through columns of b
		for j in range(len(b[0])):
			temp = 0.0
			# iterate through rows of b
			for k in range(len(b)):
				temp += a[i][k] * b[k][j]
			row.append(temp)
		result.append(row)
	return result

# Sums matrix b to matrix a
def sum_matrix(a,b):
	# Checks if matrices can be sum: m×n by m×n = m×n
	if (len(a) != len(b)) or (len(a[0]) != len(b[0])):
		raise ValueError("Matrices with these dimensions cannot be summed.")
	# iterate through rows of a
	for i in range(len(a)):
		# iterate through columns of a
		for j in range(len(a[0])):
			a[i][j] += b[i][j]
	return a

# transposes given matrix into a new matrix
def transpose(matrix):
	result = empty_matrix(len(matrix[0]),len(matrix))
	# iterate through rows
	for i in range(len(matrix)):
		# iterate through columns
		for j in range(len(matrix[0])):
			result[j][i] = matrix[i][j]
	return result

# converts a matrix to a list
def matrix2list(matrix):
	result = []
	# iterate through rows
	for i in range(len(matrix)):
		# iterate through columns 
		for j in range(len(matrix[0])):
			result.append(matrix[i][j])
	return result

# Prints the given matrix
def print_matrix(matrix):
	for r in matrix:
		print(r)