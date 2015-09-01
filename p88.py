#!/usr/bin/env python3

from itertools import product
from sys import maxsize

n = 100

def is_ascend(v):
  for i in range(len(v)-2):  
    if v[i] > v[i+1]:
      return False
  return True
    
def pi(v):
  rtv = 1
  for e in v:
    rtv *= e
  return rtv
  
def min_product_sum_aux(m, k):
  rtv = []
  for v in product(range(2,n), repeat=m):
    s, p = sum(v), pi(v)
    if p == s + ( k - m ):
      rtv.append(p)
  return min(rtv)

def min_product_sum(k):
  tmp = maxsize
  for m in range(1, k+1):
    try:
      mps = min_product_sum_aux(m, k)
      if mps < tmp:
        tmp = mps
    except ValueError:
      pass

  return tmp

if __name__ == '__main__':
  import sys
  N = int(sys.argv[1])
  
  rtv = set()
  for k in range(2, N+1):
    rtv.add(min_product_sum(k))
    