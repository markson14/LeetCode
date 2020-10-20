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
            
```

