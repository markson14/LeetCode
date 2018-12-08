import bisect
class Solution(object): # 1384ms
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for n in nums:
            m = bisect.bisect_left(dp, n) # 在dp中查找比n小的数并返回插入的index number
            if m < len(dp):
                dp[m] = n
            else:
                dp.append(n)
        
        return dp

    """
        time: 
        space:
    """
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return 0
        dp=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            lf=0
            rt=len(dp)-1
            while lf<rt:
                mid=lf+(rt-lf)//2
                if dp[mid]>=nums[i]:
                    rt=mid
                else:
                    lf=mid+1
            if lf==len(dp)-1 and dp[lf]<nums[i]:
                dp.append(nums[i])
            else:
                dp[lf]=nums[i]
        return len(dp)
