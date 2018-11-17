class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        A = A[::-1]
        for i in range(1,len(A)):
            for j in range(len(A)):
                A[i][j] += min(A[i-1][max(0,j-1) : min(len(A),j+2)])
        return min(A[-1])
