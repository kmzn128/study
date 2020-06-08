def perm(seq, k, out):
    _perm(seq, len(seq), k, [], out)

def _perm(seq, n, k, elem, out):
    le = len(elem)
#     if le > k:
#         return
    if le == k:
        out.append(elem)
        return
    for i in range(n):
        _perm(seq, n, k, elem + [seq[i]], out)
    
out = []
perm(list(range(4)), 3, out)
print(out)