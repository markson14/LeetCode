class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list_ = []
        for i in range(num+1):
            list_.append(str(bin(i))[2:].count('1'))
        return list_