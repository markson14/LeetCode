"""
  If K>1, 可以直接返回字典序最小
  否则，只能rotate整个string以获取最小字典序
"""
class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K >= 2: return ''.join(sorted(S))
        return list(S[i:]+S[:i] for i in range(len(S)))