#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.insert(0, '../scripts')

from lists import *

# Testing random list of 4000 elements multiplied by another randowm list 4000 times.
def test1():
	n = 4000
	for i in range(n):
		list1 = random_list(n)
		list2 = random_list(n)
		mult_lists(list1, list2)

# Testing random list of 100 elements expanded 4000 times.
def test2():
	n = 4000
	list = random_list(100)
	for i in range(n):
		list = expandByN(list, n)

# Testing random list of 4000 elements sumed to another randowm list 4000 times.
def test3():
	n = 4000
	for i in range(n):
		list1 = random_list(n)
		list2 = random_list(n)
		sum_lists(list1, list2)

# Testing random list of 4000 elements converted to matrix
def test4():
	n = 4000
	for i in range(n):
		list = random_list(n)
		list2matrix(list)