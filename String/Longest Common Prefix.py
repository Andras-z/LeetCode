'''Write a function to find the longest common prefix string amongst an array of strings.'''
from functools import reduce

class Solution(object):
	#use of zip
	def longestCommonPrefix(self, strs):
		if not strs:
			return ""
		for i, letter_group in enumerate(zip(*strs)):
			if len(set(letter_group)) > 1:
				return strs[0][:i]
		return min(strs)

	#use of reduce
	def longestCommonPrefix2(self, strs):
		if not strs:
			return ""
		else:
			return reduce(self.lcp, strs)

	def lcp(self, str1, str2):
		i = 0
		while(i < len(str1) and i < len(str2)):
			if str1[i] == str2[i]:
				i += 1
			else:
				break
		return str1[:i]


strs = ['Word', 'WoW', 'World']
res = Solution()
print (res.longestCommonPrefix(strs))
print (res.longestCommonPrefix2(strs))