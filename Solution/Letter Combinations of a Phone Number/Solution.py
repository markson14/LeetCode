class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ip = []
        for dig in digits:
            ip.append(dic[dig])
        res = []
        def backtracking(ip,op,res):
            if len(ip) == 1:
                for i in ip[0]:
                    res.append(op+i)
            else:
                for i in ip[0]:
                    backtracking(ip[1:], op+i, res)
        if not digits: return []
        backtracking(ip,'',res)
        return res