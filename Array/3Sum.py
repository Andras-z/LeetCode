'''Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
n = len(nums)
#[-4, -1, -1, 0, 1, 2]

#NegetiveNums = [x for x in nums if x < 0]
f = 0
for i in range(n):
	if nums[i] >= 0:
		f = i
		break
res = []
for i in range(f):
	for j in range(i+1,n-1):
		for k in range(j+1,n):
			if nums[i] + nums[j] + nums[k] == 0:
				res.append([nums[i], nums[j], nums[k]])
res = list(set(res))
print (res)