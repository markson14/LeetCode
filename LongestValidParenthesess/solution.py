class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        stack = []
        longlen,newlen = 0,0
        for i in range(l):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack != []:
                    newlen = i - stack[0]
                    if newlen > longlen:
                        longlen = newlen
                else:
                    stack.append(i)
        return longlen
        