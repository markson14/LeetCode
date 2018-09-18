class Solution:
    """
        难度：Medium
        回溯法，递归解决
    """
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtracking(list_,input_,limit_,open_,close_):
            if len(input_) == 2 * limit_:
                list_.append(input_)
            if open_ < limit_:
                backtracking(list_,input_+"(",limit_,open_+1,close_)
            if close_ < open_:
                backtracking(list_,input_+")",limit_,open_,close_+1)
        list_ = []
        backtracking(list_,'',n,0,0)
        return list_
            