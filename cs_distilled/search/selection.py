import random

li = [random.randint(0,100) for x in range(10)]

print(li)
for i in range(len(li)):
    min_ind = i
    for j in range(i+1, len(li)):
        if li[min_ind] > li[j]:
            li[j], li[min_ind] = li[min_ind], li[j]

print(li)
