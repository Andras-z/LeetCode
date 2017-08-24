'''Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].'''
nums = [5, 7, 7, 8, 8, 10]
target = 8
l = 0
r = len(nums) - 1
if r < 0 or target < nums[l] or target > nums[r]:
	return [-1, -1]
while (l <= r):
	m = int((l + r)/2)
	if target == nums[m]:
		l = r = m
		while l > 0:
			if nums[l] == nums[l-1]:
				l -= 1
			else:
				break
		while r < len(nums) - 1:
			if nums[r] == nums[r+1]:
				r += 1
			else:
				break
		return [l, r]
	elif target < nums[m]:
		r = m - 1
	else:
		l = m + 1
return [-1, -1]
