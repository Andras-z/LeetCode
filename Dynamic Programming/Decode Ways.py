'''A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

'''
class Solution(object):
	def numDecodings(self, s):
		if not s:
			return 0
		if s[0] == '0':
			return 0
		dp = [1, 1]
		for i in range(1,len(s)):
			if s[i] == '0':
				if int(s[i-1]) <= 2 and s[i-1] != '0':
					dp += [dp[-2]]
				else:
					return 0
			else:
				if int(s[i-1] + s[i]) <= 26 and s[i-1] != '0':
					dp += [dp[-1] + dp[-2]]
				else:
					dp += [dp[-1]]
		return dp[-1]

	# def numDecodings2(self, s):
	# 	return reduce(lambda (v,w,p),d:(w,(d>'0')*w+(9<int(p+d)<27)*v,d),s,(0,s>'',''))[1]*1

	def numDecodings3(self, s):
		v, w, p = 0, int(s > ''), ''
		for d in s:
			v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
		return w
	# w tells the number of ways
	# v tells the previous number of ways
	# d is the current digit
	# p is the previous digit

S = Solution()
s = '12011'
res = S.numDecodings(s)
print (res)
