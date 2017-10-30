'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
	def isValid(self, s):
		brackets = {'(':')', '{':'}', '[':']'}
		res = []
		for i in range(len(s)):
			if s[i] in brackets.keys():
				res.append(s[i])
			else:
				try:
					if brackets[res.pop()] != s[i]:
						return False
				except:
					return False
		return res == []
