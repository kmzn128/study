import random

li = [random.randint(0,100) for x in range(10)]

print(li)

def merge_sort(_list):
    if(len(_list) < 2):
        return
    mid = len(_list)//2
    list_left = _list[:mid]
    list_right = _list[mid:]

    merge_sort(list_left)
    merge_sort(list_right)

    i = j = k = 0

    while(i < len(list_left) and j < len(list_right)):
        if( list_left[i] < list_right[j]):
            _list[k] = list_left[i]
            i += 1
        else:
            _list[k] = list_right[j]
            j += 1
        k += 1

    while(i < len(list_left)):
        _list[k] = list_left[i]
        i += 1
        k += 1

    while(j < len(list_right)):
        _list[k] = list_right[j]
        j += 1
        k += 1

merge_sort(li)
print(li)
