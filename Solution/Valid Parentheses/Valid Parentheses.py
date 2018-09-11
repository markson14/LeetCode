class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if d[i]!= stack.pop():
                    return False
        if stack:
            return False
        return True