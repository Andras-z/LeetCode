nums = [2, 7, 11, 13]
Target = 9
length = len(nums)
for i in range(length):
	for j in range(i+1,length):
		if (nums[i] + nums[j]) == Target:
			ans = [i,j]
			break
return ans