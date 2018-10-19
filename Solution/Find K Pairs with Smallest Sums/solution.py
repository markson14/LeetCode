class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        for i in nums1:
            for j in nums2:
                res.append([i,j])
        res.sort(key=lambda x:x[0]+x[1])
        return res[:k]