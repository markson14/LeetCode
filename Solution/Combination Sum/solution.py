class Solution:
    """
        回溯法，找到相加等于target的子集，然后排序后添加进res
        难度：Medium
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def backtracking(cur,rest):
            if rest == 0:
                if not sorted(cur) in res:
                    res.append(sorted(cur))
            for i in candidates:
                if rest - i>= 0:
                    backtracking(cur+[i], rest-i)
        if not candidates: return []
        backtracking([],target)  
        return res