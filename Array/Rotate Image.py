'''You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''
matrix = [[1, 2, 3, 4]
		 ,[5, 6, 7, 8]
		 ,[9, 8, 7, 6]
		 ,[5, 4, 3, 2]]
n = len(matrix)
for i in range(n - 1):
	for j in range(i + 1, n):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(n):
	for j in range(int(n/2)):
		matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j] 

# most Pythonic
matrix[:] = zip(*matrix[::-1])

for i in matrix:
	print (i)