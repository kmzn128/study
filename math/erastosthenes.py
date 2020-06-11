#from collections import deque
from math import sqrt

def erasto(n):
    if(n <= 2):
        return []
    _in_list = list(range(2, n))
    out_list = []
    while(_in_list[0] < sqrt(_in_list[-1])):
        divider = _in_list.pop(0)
        out_list.append(divider)
        for elem in _in_list:
            if elem % divider == 0:
                _in_list.remove(elem)
    out_list += _in_list
    return out_list

print(erasto(30))




