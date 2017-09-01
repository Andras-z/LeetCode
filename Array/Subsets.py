'''Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution(object):
	# DFS recursively 
	def subsets1(self, nums):
	    res = []
	    self.dfs(sorted(nums), 0, [], res)
	    return res
	    
	def dfs(self, nums, index, path, res):
	    res.append(path)
	    for i in range(index, len(nums)):
	        self.dfs(nums, i+1, path+[nums[i]], res)
	        
	# Bit Manipulation    
	def subsets2(self, nums):
	    res = []
	    nums.sort()
	    for i in range(1<<len(nums)):
	        tmp = []
	        for j in range(len(nums)):
	            if i & 1 << j:  # if i >> j & 1:
	                tmp.append(nums[j])
	        res.append(tmp)
	    return res
	    
	# Iteratively
	def subsets(self, nums):
	    res = [[]]
	    for num in sorted(nums):
	        res += [item+[num] for item in res]
	    return res

nums = [1, 2, 3]
S = Solution()
ans1 = S.subsets1(nums)
ans2 = S.subsets2(nums)
ans = S.subsets(nums)
print (ans)
print (ans1)
print (ans2)