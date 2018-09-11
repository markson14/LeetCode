class Solution(object): # 108ms
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1] * n
        i2,i3,i5 = 0,0,0
        for i in range(1,n):
            ugly[i] = min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5)
            if ugly[i] == ugly[i2]*2: i2 += 1
            if ugly[i] == ugly[i3]*3: i3 += 1
            if ugly[i] == ugly[i5]*5: i5 += 1
        return ugly[-1]