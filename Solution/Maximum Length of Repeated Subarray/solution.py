class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]
        for i in range(len(A)-1,-1,-1):
            for j in range(len(B)-1,-1,-1):
                if A[i] == B[j]:
                    dp[j][i] = dp[j+1][i+1] + 1
        max_ = 0
        for row in dp:
            max_ = max(max(row), max_)
        return max_