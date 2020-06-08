def subset(data):
    for i in range(len(data)+1):
        yield from comb(data, i, 0, [])

def comb(data, r, start, progress):
  if r == 0:
    yield progress
    return

  for i in range(start, len(data)):
    yield from comb(data, r - 1, i + 1, progress + [data[i]])
    
for e in subset('ABCD'):
    print(e)