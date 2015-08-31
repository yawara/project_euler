def reccuring_size(n):
  
  q, r = 0, 1
  print(q, ".", sep="", end="")
  
  rs = []
  rs.append(r)
    
  while True:
    q, r = (r*10)//n, (r*10)%n
    print(q, sep="", end="")
    if r == 0:
      print("")
      return 0
    else:
      for i, b in enumerate(rs):
        if r == b:
          print("")
          return len(rs)-i
      rs.append(r)

if __name__ == "__main__":
  max_d, max_len = 0, 0 
  
  for d in range(2, 1000):
    tmp = reccuring_size(d)
    if tmp > max_len:
      max_d, max_len = d, tmp 
  
  print(max_d, max_len)