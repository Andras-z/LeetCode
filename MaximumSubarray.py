nums = [-2,1,-3,4,-1,2,1,-5,4]
maxsum = cursum = nums[0]
for num in nums[1:]:
	cursum = max(num, cursum + num)
	maxsum = max(cursum, maxsum)
print (maxsum)