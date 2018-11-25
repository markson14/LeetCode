class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        if not tokens or not P:
            return 0
        res = 0
        tokens = sorted(tokens)
        while len(tokens)>1:
            if res > 0 and P < tokens[0]:
                res -= 1
                P += tokens.pop()
            elif P >= tokens[0]:
                res += 1
                P -= tokens.pop(0)
            else:
                break
        if P >= tokens[0]:
            res += 1
        return res