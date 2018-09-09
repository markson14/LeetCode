class Solution(object):
    def dfs(self,nums,index):
        if index == len(nums):
            self.res +=1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums,index):
                self.dfs(nums,index+1)
    def valid(self,nums,index):
        for i in range(index):
            if nums[i] == nums[index] or abs(nums[i]-nums[index]) == index-i:
                return False
        return True
            
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.dfs([-1]*n,0)
        return self.res
            