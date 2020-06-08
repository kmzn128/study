def comb(data, r, start, progress):
    if r == 0:
        yield progress

    for i in range(start, len(data)):
        print("i={0}".format(i))
        print("r={0}".format(r))
        yield from comb(data, r - 1, i + 1, progress + [data[i]])
    
for e in comb("ABCD", 3, 0, []):
    print(e)