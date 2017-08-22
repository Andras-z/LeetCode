nums1 = [1,3,5,7,9]
m = 5
nums2 = [2,4,6,8,10]
n = 5
if m == 0:
    nums1 = []
if n == 0:
    nums2 = []
nums1.extend(nums2)
nums1.sort()
print (nums1)
