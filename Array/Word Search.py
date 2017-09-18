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
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    coordinate = [[0 for col in range(len(board[0]))] for row in range(len(board))]
                    if self.Search(i, j, board, word, 1, coordinate):
                        return True
        return False

    def Search(self, x, y, board, word, W, coordinate):
        if W == len(word):
            return True
        coordinate[x][y] = 1
        if x - 1 >= 0:
            if board[x - 1][y] == word[W] and coordinate[x - 1][y] == 0:
                if self.Search(x - 1, y, board, word, W + 1, coordinate):
                    return True
        if x + 1 < len(board):
            if board[x + 1][y] == word[W] and coordinate[x + 1][y] == 0:
                if self.Search(x + 1, y, board, word, W + 1, coordinate):
                    return True
        if y - 1 >= 0:
            if board[x][y - 1] == word[W] and coordinate[x][y - 1] == 0:
                if self.Search(x, y - 1, board, word, W + 1, coordinate):
                    return True
        if y + 1 < len(board[0]):
            if board[x][y + 1] == word[W] and coordinate[x][y + 1] == 0:
                if self.Search(x, y + 1, board, word, W + 1, coordinate):
                    return True
        coordinate[x][y] = 0
        return False

board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'E', 'S'],
         ['A', 'D', 'E', 'E']]
word = "ABCESEEDASF"

S = Solution()

print (S.exist(board, word))
