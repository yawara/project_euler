#!/usr/bin/env python3
from pyprimes import factorise
from cypari.all import pari
import sys

def pari_phi(n):
  return int(pari(n).phi())
  
def phi(n):
  rtv = 1
  for p, k in factorise(n):
    rtv *= p**(k-1) * (p-1)
  return rtv

def n_over_phi(n):
  rtv = 1
  for p, k in factorise(n):
    rtv *= p / ( p - 1 )
  return rtv
  
def digits(n):
  rtv = [ 0 for i in range(10) ]
  
  tmp = n
  while True:
    rtv[tmp%10] += 1
    tmp //= 10
    if tmp == 0:
      return rtv
  
if __name__ == "__main__":
  r = sys.maxsize
  rtv = 0
  
  N = int(sys.argv[1])
  
  for n in range(2, N):
    phi_n = pari_phi(n)
    if digits(n) == digits(phi_n):
      n_o_phi = n / phi_n
      if n_o_phi < r:
        r, rtv = n_o_phi, n
  
  print(rtv, r)