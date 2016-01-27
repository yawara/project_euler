from sage.all import *

N = 12000
M = 50000

rtv = []

for n in range(2, M):
    for p in Partitions(n):
        if sum(p) == prod(p):
            
