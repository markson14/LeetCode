class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        rec = {}
        n = len(A)
        for i in range(n):
            for j in range(n):
                sum1 = A[i] + B[j]
                if not sum1 in rec:
                    rec[sum1] = 1
                else:
                    rec[sum1] +=1
        ans = 0
        for i in range(n):
            for j in range(n):
                sum2 = C[i] + D[j]
                if -sum2 in rec:
                    ans += rec[-sum2]
        return ans
       