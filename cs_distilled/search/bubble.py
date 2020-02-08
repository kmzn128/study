import random

li = [random.randint(0,100) for x in range(10)]

print(li)
for i in range(len(li)):
    for j in range(0, len(li)-i-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

print(li)