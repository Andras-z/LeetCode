nums = [1,1,2]
L = 0
for i in range(1,len(nums)):
	if nums[i] != nums[L]:
		L += 1
		nums[L] = nums[i]
print (L + 1)
