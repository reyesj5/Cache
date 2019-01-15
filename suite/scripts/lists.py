#!/usr/bin/env python
# coding=utf-8

import random
import math

#!/usr/bin/env python
# coding=utf-8

# Creates a list of size n filled with 0's
def empty_list(n):
	list = []
	for i in range(n):
		list.append(0)
	return list


# returns a matrix of size n filled with random values between 1-4000
def random_list(n):
	elements = random.sample(range(4000), n)
	return elements

# multiplies two lists by each other
def mult_lists(list1,list2):
	result = []
	for i in range(min(len(list1), len(list2))):
		result.append(list1[i] * list2[i])
	return result


# duplicates and appends the list to itself n times.
def expandByN(list, n):
	if n > 0:
		dup = list[:]
		return expandByN(list + dup, n - 1)
	else:
		return list


# Sums list b to list a
def sum_lists(list1,list2):
	result = []
	for i in range(min(len(list1), len(list2))):
		result.append(list1[i] + list2[i])
	return result

# converts a list to a square matrix truncating if the list is not a perfect square
def list2matrix(list):
	size = int(math.sqrt(len(list)))
	result = []
	for i in range(size):
		row = []
		for j in range(size):
			row.append(list[(i*size + j)])
		result.append(row)
	return result