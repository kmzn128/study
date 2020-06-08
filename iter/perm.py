def listExcludedIndices(data, indices=[]):
  return [x for i, x in enumerate(data) if i not in indices]

def perm(data, r, progress):
  if r == 0:
    yield progress
    return

  for i in range(len(data)):
    yield from perm(listExcludedIndices(data,[i]), r - 1, progress + [data[i]])
    
for e in perm("ABC", 3, []):
    print(e)