class Solution:
    """
        滑动窗口经典用法，先建立窗口。然后每次减去第一个，加上下一个来拓展。
    """
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        key = sum(map(hash,s1))
        now = sum(map(hash,s2[:m]))
        if key == now: return True
        for i in range(m,n):
            now = now - hash(s2[i-m]) + hash(s2[i])
            if now == key:
                return True
        return False