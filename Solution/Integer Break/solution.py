class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 : return 0
        if n <= 2 : return 1
        if n == 3 : return 2
        count = 0
        while n > 4:
            n -= 3
            count += 1
        return pow(3,count)*n