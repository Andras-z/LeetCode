'''Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		maxLength = 0
		cur = []
		for i in range(len(s)):
			if s[i] in cur:
				cur.append(s[i])
				cur[:] = cur[cur.index(s[i]) + 1 :]
			else:
				cur.append(s[i])
			if len(cur) > maxLength:
				maxLength = len(cur)
		return maxLength
res = Solution()
s = "pwwkew"
print (res.lengthOfLongestSubstring(s))