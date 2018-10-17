class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in S:
            if not stack:
                stack.append(i)
            else:
                if i == ")" and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)