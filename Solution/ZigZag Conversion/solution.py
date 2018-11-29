class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        k = (numRows-1)*2
        res = [[] for _ in range(numRows)]
        for i in range(len(s)):
            tmp = abs(i%k - numRows+1)
            if tmp >= numRows:
                tmp = 0
            res[tmp].append(s[i])
        res = res[::-1]
        res = sum(res,[])
        return ''.join(res)

from itertools import chain,cycle
class Solution2:
    def convert(self, s, N):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lines = [''] * N
        levels = chain(range(N), range(N - 2, 0, -1))        
        for i, s in zip(cycle(levels), s):
            lines[i] += s
            
        return ''.join(lines)