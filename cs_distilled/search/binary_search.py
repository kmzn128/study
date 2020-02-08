def binary_search(target, left, right, nums):
    if(left > right):
        return -1
    mid = (right-left)//2 + left
    if(nums[mid] == target):
        return mid
    elif(nums[mid] < target):
        return binary_search(target, mid+1, right, nums)
    else:
        return binary_search(target, left, mid-1, nums)

nums = [2,4,6,7,9,12]
    
print(binary_search(7,0,len(nums)-1, nums))