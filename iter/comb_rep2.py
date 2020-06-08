def comb(seq, k, out):
    _comb(seq, len(seq), k, 0, [], out)

def _comb(seq, n, k, i, elem, out):
    le = len(elem)
    if le == k:
        out.append(elem)
        return
    for i in range(i, n):
        _comb(seq, n, k, i, elem + [seq[i]], out)
    
out = []
comb(list(range(4)), 3, out)
print(out)