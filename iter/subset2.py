def subset(seq, out):
    for i in range(len(seq)+1):
        subout = []
        comb(seq, i, subout)
        out += subout

def comb(seq, k, out):
    _comb(seq, len(seq), k, 0, [], out)

def _comb(seq, n, k, i, elem, out):
    le = len(elem)
    if le == k:
        out.append(elem)
        return
    for i in range(i, n):
        _comb(seq, n, k, i+1, elem + [seq[i]], out)
    
out = []
subset(list(range(3)), out)
print(out)