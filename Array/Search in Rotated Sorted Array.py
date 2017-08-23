'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.'''
nums = [1,3,5]
target = 4
if not nums:
	return -1
f = 0
for i in range(1, len(nums)):
	if nums[i] < nums[i-1]:
		f = i
		break
if f == 0:
	if target < nums[0] or target > nums[-1]:
		return -1
	l = 0; r = len(nums) - 1
	while(l <= r):
		m = int((l + r) / 2)
		if target == nums[m]:
			return m
		if target < nums[m]:
			r = m - 1
		else:
			l = m + 1
else:
	if target < nums[f] or target > nums[f-1] or (target < nums[0] and target > nums[-1]):
		return -1
	if target >= nums[0]:
		l = 0; r = f - 1
		while (l <= r):
			m = int((l + r) / 2)
			if target == nums[m]:
				return m
			if target < nums[m]:
				r = m - 1
			else:
				l = m + 1
	elif target >= nums[f]:
		l = f; r = len(nums) - 1
		while (l <= r):
			m = int((l + r) / 2)
			if target == nums[m]:
				return m
			if target < nums[m]:
				r = m - 1
			else:
				l = m + 1
return -1


#Discuss
if not nums:
    return -1

low, high = 0, len(nums) - 1

while low <= high:
    mid = (low + high) / 2
    if target == nums[mid]:
        return mid

    if nums[low] <= nums[mid]:
        if nums[low] <= target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1

return -1