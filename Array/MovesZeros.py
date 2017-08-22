'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.'''
nums = [0, 1, 0, 3, 12]
i = 0
count = 0
for num in nums:
	if num != 0:
		nums[i] = num
		i += 1
	else:
		count += 1
for i in range(count):
	nums[len(nums) - i - 1] = 0
print (nums)


zero = 0  # records the position of "0"
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1