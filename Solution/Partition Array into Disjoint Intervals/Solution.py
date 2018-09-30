
class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        curmax = 0
        dp = [A[-1] for _ in range(n)]
        for i in range(n-2,-1,-1):
            dp[i] = min(dp[i+1], A[i])
        for i in range(n):
            curmax = max(curmax,A[i])
            if curmax <= dp[i+1]:
                return i+1