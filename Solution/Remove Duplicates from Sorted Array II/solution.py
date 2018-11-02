import collections
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        res = []
        for i,c in c.items():
            p = c - 2
            if p > 0:
                while p:
                    nums.remove(i)
                    p -= 1

        
                    