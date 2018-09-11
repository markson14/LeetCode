class Solution(object):
    """
        如果含有重复的话，s在（s+s）里去头去尾后应该存在子字符串
    """
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]