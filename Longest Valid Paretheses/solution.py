class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        last = -1
        res = 0
        for i in range(len(s)):
            if s[i] == '(': stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        res = max(res, i - stack[-1])
                    else:
                        res = max(res, i - last)
                else:
                    last = i
        return res