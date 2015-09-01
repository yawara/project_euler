from sage.all import *

n = 2
while True:
    print(n)
    p = Partitions(n)
    if p.cardinality() % 1000000 == 0:
        print(p)
        print(p.cardinality())
        break
    n += 1
