def perm_rep(data, r, progress):
  if r == 0:
    yield progress
    return

  for i in range(len(data)):
    yield from perm_rep(data, r - 1, progress + [data[i]])
    
for e in perm_rep("ABC", 3, []):
    print(e)