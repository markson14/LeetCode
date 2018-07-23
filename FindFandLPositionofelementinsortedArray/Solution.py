class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not target in nums:
            return[-1,-1]
        
        l=[]
        a = nums.index(target)
        l.append(a)
        
        res = nums[a:]
        x = 0
        for i in range(len(res)):
            if res[i] == target:
                x = max(i+a,x)
        l.append(x)

        return l
            