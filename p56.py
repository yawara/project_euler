#!/usr/bin/env python3

def digital_sum(n):
  tmp = n
  rtv = []
  while True:
    if tmp == 0:
      return sum(rtv)
    rtv.append(tmp % 10)
    tmp //= 10
    
if __name__ == '__main__':
  rtv = []
  for a in range(2,100):
    for b in range(1,100):
      rtv.append(digital_sum(a**b))
  
  print(a,b,max(rtv))