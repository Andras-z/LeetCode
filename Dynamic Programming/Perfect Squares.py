'''Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''
class Solution(object):
	def numSquares(self, n):
		d = [0] * (n + 1) 
		Square = 2
		for i in range(1,n + 1):
			if i == Square ** 2:
				d[i] = 1
				Square += 1
			else:
				d[i] = d[i - (Square - 1) ** 2] + 1
		return d[-1]
res = Solution()
print (res.numSquares(12))
'''
1 = 1 => 1
2 = 1 + 1 => 2
3 = 1 + 1 + 1 => 3
4 = 4 => 1
5 = 1 + 4 => 2
6 = 1 + 1 + 4 => 3
7 = 1 + 1 + 1 + 4 => 4
8 = 4 + 4 => 2
9 = 9 => 1
10 = 1 + 9 => 2
11 = 1 + 1 + 9 => 3
12 = 4 + 4 + 4 => 3
13 = 4 + 9 => 2
'''