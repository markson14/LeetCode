class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        dp = [0 for _ in range(len(A))]
        for i in range(2,len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] += dp[i-1] + 1
                count += dp[i]
        return count