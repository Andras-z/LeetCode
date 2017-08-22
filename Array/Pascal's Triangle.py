numRows = 5
# ans = []
# for i in range(numRows):
# 	if i == 0:
# 		ans.append([1])
# 		continue
# 	if i == 1:
# 		ans.append([1,1])
# 		continue
# 	ans.append([])
# 	for j in range(i+1):
# 		if j == 0:
# 			ans[i].append(1)
# 			continue
# 		if j == i:
# 			ans[i].append(1)
# 			continue
# 		ans[i].append(ans[i-1][j-1] + ans[i-1][j])
# print (ans)

# res = [[1]]
# for i in range(1, numRows):
#     res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
# print (res[:numRows])

row = [1]
for _ in range(numRows):
    row = [x + y for x, y in zip([0]+row, row+[0])]
print (row)