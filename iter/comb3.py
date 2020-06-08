def comb(seq, k):
    yield from _comb(seq, len(seq), k, 0, [])

def _comb(seq, n, k, i, elem):
    le = len(elem)
#     print("print",elem)
    if le == k:
#         print("yield")
        yield elem
#     print("le=", le)
    for i in range(i, n):
#         print("i=", i)
        yield from  _comb(seq, n, k, i+1, elem + [seq[i]])
    
for e in comb(list(range(4)), 3):
    print(e)