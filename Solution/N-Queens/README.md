# N Queens II

The *n*-queens puzzle is the problem of placing *n* queens on an *n*×*n* chessboard such that no two queens attack each other.

![img](https://leetcode.com/static/images/problemset/8-queens.png)

Given an integer *n*, return the number of distinct solutions to the *n*-queens puzzle.

**Example:**

```
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

------





```python
class Solution(object):
    def dfs(self,nums,index):
        if index == len(nums):
            self.res +=1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums,index):
                self.dfs(nums,index+1)
    def valid(self,nums,index):
        for i in range(index):
            if nums[i] == nums[index] or abs(nums[i]-nums[index]) == index-i:
                return False
        return True
            
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.dfs([-1]*n,0)
        return self.res
      
      
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
```

