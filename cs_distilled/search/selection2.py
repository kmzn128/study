def selection(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] > nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
                
    return nums

import random
nums = [random.randint(-100, 100) for i in range(10)]

print(selection(nums))