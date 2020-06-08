def comb_rep(data, r, start, progress):
  if r == 0:
    yield progress
    return

  for i in range(start, len(data)):
    yield from comb_rep(data, r - 1, i, progress + [data[i]])
    
for e in comb_rep("ABC", 3, 0, []):
    print(e)