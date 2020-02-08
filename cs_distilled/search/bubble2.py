def bubble(nums):
    for i in range(len(nums)-1):
        for j in range(i, len(nums)-1):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                
    return nums

import random
nums = [random.randint(-100, 100) for i in range(10)]

print(bubble(nums))