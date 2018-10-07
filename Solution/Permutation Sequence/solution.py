import itertools
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = ''
        for j in range(1,n+1):
            nums+=str(j)
        count = 0
        for i in itertools.permutations(nums):
            count += 1
            if count == k:
                return ''.join(i)