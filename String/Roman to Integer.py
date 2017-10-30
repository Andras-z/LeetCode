'''Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

I:1, V:5, X:10, L:50, C:100, D:500, M:1000

'''
class Solution(object):
	def romanToInt(self, s):
		length = len(s)
		nums = []
		roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
		for i in range(length):
			nums.append(roman[s[i]])
		for i in range(1,length):
			if nums[i] > nums[i-1]:
				nums[i-1] *= -1
		return sum(nums)
		"""
		:type s: str
		:rtype: int
		"""
s = "MCMXCIX"
res = Solution()
print (res.romanToInt(s))