def raising(t):
  if t == ():
    return set([(1,)])
  else:
    rtv = set()
    lt = list(t)
    rtv.add(tuple([1] + lt))

    for i in range(len(lt)-1):
      if lt[i] < lt[i+1]:
        tmp = lt.copy()
        tmp[i] += 1
        rtv.add(tuple(tmp))

    lt[-1] += 1
    rtv.add(tuple(lt))

    return rtv

def raising_s(ts):
  rtv = set()
  
  for t in ts:
    for rt in raising(t):
      rtv.add(rt)
    
  return rtv

def young(n):
  rtv = set([()])
  for i in range(n):
    rtv = raising_s(rtv)
  return rtv

def p(n):
  return len(young(n))

if __name__ == '__main__':
  n = 2
  yt = young(2)
  while True:
    print(n, len(yt))
    if len(yt) % 1000000 == 0:
      break
    n += 1
    yt = raising_s(yt)
    
  print(n)