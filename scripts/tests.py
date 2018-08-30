#!/usr/bin/env python
# coding=utf-8

from matrices import *
import cProfile
import re
import time

# Measuring how long a script runs
start = time.time()

X = [[12,7],
    [4 ,5],
    [3 ,8]]

print_matrix(empty_matrix(5,4))
print_matrix(identity(5))
print_matrix(transpose(X))
print_matrix(mult(X, identity(2)))
print_matrix(sum(X,X))
cProfile.run('transpose("X")')

print 'Script took', time.time()-start, 'seconds.'