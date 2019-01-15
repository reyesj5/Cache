#!/usr/bin/env python
# coding=utf-8
"""
Produces load on all available CPU cores
Source: https://gist.github.com/tott/3895832
"""

from multiprocessing import Pool
from multiprocessing import cpu_count

def f(x):
    while True:
        x*x

def load_cpu():
    processes = cpu_count()
    print 'utilizing %d cores\n' % processes
    pool = Pool(processes)
    pool.map(f, range(processes))