class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        for a in range(len(A)):
            A[a] = list(map(str,A[a]))
        
        A_T = list(zip(*A))
        
        c = 0
        
        for row in A_T:
            if list(row) != sorted(row):
                c += 1
        return c