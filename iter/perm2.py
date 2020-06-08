def listExcludedIndices(seq, indices=[]):
  return [x for i, x in enumerate(seq) if i not in indices]

def perm(seq, k, out):
    _perm(seq, len(seq), k, [], out)

def _perm(seq, n, k, elem, out):
    le = len(elem)
    if le == k:
        out.append(elem)
        return
    for i in range(len(seq)):
        l = listExcludedIndices(seq, [i])
#         print("l = ", l)
        _perm(l, n, k, elem + [seq[i]], out)
    
out = []
perm(list(range(4)), 3, out)
print(out)