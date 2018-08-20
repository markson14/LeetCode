# Solutoin1 (554ms)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sq = [i**2 for i in range(1,int(n**0.5)+1)]
        depth = 0
        cur = [0]
        while True:
            nxlev = []
            for i in cur:
                for j in sq:
                    if i+j == n: return (depth+1)
                    if i+j < n: nxlev.append(i+j)
            cur = list(set(nxlev))
            depth += 1
        return depth