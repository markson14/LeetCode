class Solution:
    """
        回溯法，若剩余list长度等于1，则将rest+result添加进输出结果list里面。
        难度： Medium
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtracking(rest, result):
            if len(rest)==1:
                res.append(rest+result)
            for i,c in enumerate(rest):
                backtracking(rest[:i]+rest[i+1:],result+[c])
        backtracking(nums,[])
        return res
            
                