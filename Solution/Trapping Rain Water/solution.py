class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        双指针，是solution2的空间优化版本
        runtime:52ms
        """
        water = 0
        left_max = 0
        right_max = 0
        l = 0
        r = len(height)-1
        while l<r:
            left_max = max(left_max,height[l])
            right_max = max(right_max,height[r])
            if left_max < right_max:
                water += left_max - height[l]
                l+=1
            else:
                water += right_max - height[r]
                r-=1
        return water

class Solution1:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int'
        runtime: 76ms
        """
        if not height: return 0
        water = 0
        MaxIndex = height.index(max(height))
        prev = 0
        for i in range(MaxIndex):
            if height[i] > prev:
                water += (height[i]-prev)*(MaxIndex-i)
                prev = height[i]
            water -= height[i]
        prev = 0
        for i in range(len(height)-1,MaxIndex,-1):
            if height[i] > prev:
                water += (height[i]-prev)*(i-MaxIndex)
                prev = height[i]
            water -= height[i]
        return water

class Solution2:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        runtime: 44ms
        """
        left_max = []
        right_max = []
        water = 0
        
        prev = -1
        for i in range(len(height)):
            if height[i] > prev:
                left_max.append(height[i])
                prev = height[i]
            else:
                left_max.append(prev)
                
        prev = -1
        for i in range(len(height)-1,-1,-1):
            if height[i] > prev:
                right_max.append(height[i])
                prev = height[i]
            else:
                right_max.append(prev)
        right_max = right_max[::-1]
        
        for i in range(len(height)):
            water += min(left_max[i],right_max[i]) - height[i]
        return water
        