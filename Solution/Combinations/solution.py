import itertools
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,n+1)]
        return [i for i in itertools.combinations(nums,k)]

class Solution1:
    def dfs(self,start,path,ans,n,k):
        if len(path)==k:
            ans.append(path)
        for i in range(start,n+1):
            self.dfs(i+1,path+[i],ans,n,k)
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(1,[],ans,n,k)
        return ans