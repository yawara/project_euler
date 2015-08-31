from collections import defaultdict
import math
import pyprimes

def primes_below(n):
  rtv = []
  num_table = defaultdict(bool)
  for i in range(2, n+1):
    if not num_table[i]:
      rtv.append(i)
      for j in range(1, (n+1)//i+1):
        num_table[i*j] = True
  return rtv

def is_square(n):
  if n == 1:
    return 1, True
  
  for k in range(2, int(math.sqrt(n))+1):
    if n == k**2:
      return k, True
  return None, False

if __name__ == '__main__':
  primes = primes_below(1000000)
  
  n = 100000
  
  pp = 0
  for i in range(1, n):
    m = 2 * i + 1
    
    while primes[pp] < m:
      pp += 1
      
    if primes[pp] == m:
      pass
    else:
      flag = False
      for p in primes[1:pp]:
        q = ( m - p ) // 2
        k, is_s = is_square(q)
        if is_s:
          assert m == p + 2 * k**2
          flag = True
          break
      
      if not flag:
        print("TERMINATED")
        print(m)
        break