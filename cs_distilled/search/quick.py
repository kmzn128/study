import random

#li = [random.randint(0,100) for x in range(10)]
nums = [8,4,3,7,6,5,2,1]

print(nums)

def quick_sort(left, right, nums):
    if( left < right ):
        i = left
        j = right
        mid = (j-i)//2+i
        pivot = nums[mid]
        while(True):
            while(nums[i] < pivot):
                i += 1
            while(nums[j] > pivot):
                j -= 1
            if(i >= j):
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        quick_sort(left, i-1, nums)
        quick_sort(j+1, right, nums)

quick_sort(0, len(nums)-1, nums)
print(nums)

