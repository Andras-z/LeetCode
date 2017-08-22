nums = [1,2,5,7]
target = 4
for i in range(len(nums)):
	if target < nums[i]:
		return i
return len(nums)