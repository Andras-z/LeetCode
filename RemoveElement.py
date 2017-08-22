nums = [3,3,3,3,3,3,3,3,3,3]
val = 3
newTail = 0
for i in range(len(nums)):
	if nums[i] != val:
		nums[newTail] = nums[i]
		newTail += 1
print (newTail)
print (len(nums))