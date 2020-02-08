def radix(nums, max):
    shift = 0
    bit_max = max.bit_length()
    while(shift <= bit_max):
        new_list_odd = []
        new_list_even = []
        for e in nums:
            shifted_e = e >> shift
            if shifted_e % 2 == 0:
                new_list_even.append(e)
            else:
                new_list_odd.append(e)
        nums = new_list_even + new_list_odd
        shift += 1
    return nums           

import random
max = 100
nums = [random.randint(0, max) for i in range(30)]


print(radix(nums, max))