'''Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.'''
# prices = [7, 1, 5, 3, 6, 4]
# maxNum = 0
# minNum = prices[0]
# for num in prices[1:]:
# 	if num < minNum:
# 		minNum = num
# 		continue
# 	if num - minNum > maxNum:
# 		maxNum = num - minNum
# print (maxNum)

'''Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).'''

prices = [1, 2]
temp = [x - y for x , y in zip(prices[1:] , prices[:-1])]
ans = sum([x for x in temp if x > 0])
print (ans)

for i in range(1,len(prices)):
	if prices[i] > prices[i-1]:
		ans += prices[i] - prices[i-1]