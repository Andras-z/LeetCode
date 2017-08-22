'''Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?'''
nums = [0]
nums.append(len(nums))
nums.sort()
if nums[0] != 0:
	print (0)
for i in range(1,len(nums)):
    if nums[i] - nums[i-1] != 1:
        print (nums[i] - 1)
print (nums[-1])

n = len(nums)
return n * (n+1) / 2 - sum(nums)