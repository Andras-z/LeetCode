'''Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

'''
class Solution(object):
	def maxProduct(self, nums):
		if not nums:
			return 0
		if len(nums) == 1:
			return nums[0]
		now = negative = 1
		last = maxPro = nums[0]
		for num in nums:
			if num > 0:
				now *= num
				maxPro = max(maxPro, now)
			else:
				negative *= num
				if negative > 0:
					now = last * now * negative
					negative = 1
					maxPro = max(maxPro, now)
				else:
					last, now = now, 1
					maxPro = max(maxPro, last)
		return maxPro

	def maxProduct2(self, nums):
		maximum = big = small = nums[0]
		for n in nums[1:]:
			big, small = max(n, n*big, n*small), min(n, n*big, n*small)
			maximum = max(maximum, big)
		return maximum

S = Solution()
nums = [2, 3, -2, 4]
res = S.maxProduct(nums)
print (res)