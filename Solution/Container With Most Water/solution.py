class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l,r = 0,len(height)-1
        res = 0
        while l != r:
            w = r - l
            if height[l] < height[r]:
                h = height[l]
                l+=1
                # h = height[l]
            else:
                h = height[r]
                r-=1
                # h = height[r]
            if res < w*h:
                res = w*h
        return res
        