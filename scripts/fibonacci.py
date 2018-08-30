#!/usr/bin/env python
# coding=utf-8

from math import sqrt

# return nth fibonacci number
def fib(n):
  if (n==0):
    return 0
  elif (n==1):
    return 1
  else:
    return fib(n-1) + fib(n-2)

# efficient math formula for fib
def fib2(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))