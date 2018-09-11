class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax, curend, m,c = 0,0,len(nums)-1,0
        for i in range(m):
            curmax = max(curmax, i+nums[i])
            if i == curend:
                c+=1
                curend = curmax
        return c