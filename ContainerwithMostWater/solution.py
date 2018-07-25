class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        max_height = 0
        i, j = 0, len(height)-1
        
        while i < j:
            if height[i] < height[j]:
                n = height[i]
                i+=1
            else:
                n = height[j]
                j-=1
            if n > max_height:
                max_area = max(max_area, n*(j-i+1))
        return max_area