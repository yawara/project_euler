#!/usr/bin/env python3
from pyprimes import factorise
from itertools import permutations
from collections import defaultdict
import sys

def phi(n):
  rtv = n
  for p, k in factorise(n):
    rtv *= ( 1 - 1/p )
  return int(rtv)

def digits(n):
  rtv = [ 0 for i in range(10) ] 
  for d in str(n):
    rtv[int(d)] += 1
  return rtv
  
if __name__ == "__main__":
  r = sys.maxsize
  rtv = 0
  
  N = int(sys.argv[1])
  
  for n in range(2, N):
    phi_n = phi(n)
    if digits(n) == digits(phi_n):
      n_phi_n = n / phi_n
      if n_phi_n < r:
        r, rtv = n_phi_n, n
  
  print(rtv, r)