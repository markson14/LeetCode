class Solution:
    """
        边界情况问题，在flowerbed两边各增加[0]，即可直接通过遍历得到结果
    """
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0]
        m = len(flowerbed)
        for i in range(1,m-1):
            if flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] != 1:
                flowerbed[i] = 1
                count += 1
        return count >= n