class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        
        二分幂，分n>=0,n<0两种情况讨论
        """
        res = 1
        if n > 0:
            while n != 0:
                if n % 2 == 1:
                    res *= x
                n //= 2
                x *= x
        else:
            n = -n
            while n != 0:
                if n % 2 == 1:
                    res *= x
                n //= 2
                x *= x
            res = 1/res
        return res