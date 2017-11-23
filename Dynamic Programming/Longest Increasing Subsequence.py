'''Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''
class  Solution(object):
	#O(n^2) DP
	def lengthOfLIS(self, nums):
		if not nums:
			return 0
		dp = [1] * len(nums)
		maxLength = 1
		for i in range(1,len(nums)):
			for j in range(i):
				if nums[j] < nums[i]:
					dp[i] = max(dp[i], dp[j] + 1)
		return max(dp)

	#using binary search :O(nlogn)
	def lengthOfLIS2(self, nums):
		def search(temp, left, right, target):
			if left == right:
				return left
			mid = left+(right-left)/2
			return search(temp, mid+1, right, target) if temp[mid]<target else search(temp, left, mid, target)
		temp = []
		for num in nums:
			pos = search(temp, 0, len(temp), num)
			if pos >=len(temp):
				temp.append(num)
			else:
				temp[pos]=num
		return len(temp)

S = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18, 6]
print (S.lengthOfLIS(nums))
