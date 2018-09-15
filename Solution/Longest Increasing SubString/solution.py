class Solution(object): # 1384ms
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    res[i] = max(res[i],res[j]+1)
        return max(res)



    """
        time: 
        space:
    """

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
