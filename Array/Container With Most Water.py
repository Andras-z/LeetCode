'''Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.'''
height = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = 0
r = len(height) - 1
maxarea = 0
while(l < r):
	maxarea = max(maxarea, min(height[l], height[r])*(r-l))
	if height[l] < height[r]:
		l += 1
	else:
		r -= 1
print (maxarea)