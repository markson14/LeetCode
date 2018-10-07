class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        leftview = [max(row) for row in grid]
        topview = [max(col) for col in zip(*grid)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += min(leftview[i], topview[j]) - grid[i][j]
        return count