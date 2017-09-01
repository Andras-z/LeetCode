'''Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
class Solution(object):
    def exist(self, board, word):
    	for i in range(len(board)):
    		print (1)
    		for j in range(len(board[0])):
    			if board[i][j] == word[0]:
    				print (0)
    				if self.Search(i, j, board, word, 1):
    					return True
    	return False

    def Search(self, x, y, board, word, W):
    	if W == len(word):
    		return True
    	board[x][y] = ''
    	if x - 1 >= 0:
    		if board[x - 1][y] == word[W]:
    			if self.Search(x - 1, y, board, word, W + 1):
    				return True
    	if x + 1 < len(board):
    		if board[x + 1][y] == word[W]:
    			if self.Search(x + 1, y, board, word, W + 1):
    				return True
    	if y - 1 >= 0:
    		if board[x][y - 1] == word[W]:
    			if self.Search(x, y - 1, board, word, W + 1):
    				return True
    	if y + 1 < len(board[0]):
    		if board[x][y + 1] == word[W]:
    			if self.Search(x, y + 1, board, word, W + 1):
    				return True
    	return False

board = [
		 ['C', 'A', 'A'],
		 ['A', 'A', 'A'],
		 ['B', 'C', 'D']		
]
word = "AAB"

S = Solution()

print (S.exist(board, word))