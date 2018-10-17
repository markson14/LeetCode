class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for i,c in enumerate(A):
            if c % 2 == 0:
                even.append(c)
            else:
                odd.append(c)
        res = []
        for i in range(len(even)):
            res.extend([even[i],odd[i]])
        return res