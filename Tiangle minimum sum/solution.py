class Solution(object): #32ms
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth = len(triangle)
        for i in range(1, depth):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1])
        return min(triangle[-1])        