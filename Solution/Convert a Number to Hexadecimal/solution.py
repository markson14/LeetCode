class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return hex(4294967296+num)[2:]
        else:
            return hex(num)[2:]