#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ['.' * n for _ in range(n)]
        def backtrack(board, row):
            if row == len(board):
                res.append(board[::])
            for i in range(n):
                if not is_valid(i, row):
                    continue
                board[row] = board[row][:i] + 'Q' + board[row][i+1:]
                backtrack(board, row+1)
                board[row] = board[row][:i] + '.' + board[row][i+1:]
        
        def is_valid(col, row):
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            for i in range(1, row+1):
                # print(row-i, col-i)
                if col-i >=0 and board[row-i][col-i] == 'Q':
                    return False
                if col+i < n and board[row-i][col+i] == 'Q':
                    return False
            return True

        backtrack(board, 0)
        return res
                

# @lc code=end

