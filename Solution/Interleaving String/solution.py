import numpy as np
class Solution:
        """
        Time: m*n
        Space: m*n

        """
        def isInterleave(self, s1, s2, s3):
            """
            :type s1: str
            :type s2: str
            :type s3: str
            :rtype: bool
            """
            if len(s1) + len(s2) != len(s3):
                return False
            match = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
            match[0][0] = True
            for i in range(1, len(s1) + 1):
                match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]
            for i in range(1, len(s1) + 1):
                for j in range(1, len(s2) + 1):
                    match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])
            return np.array(match)
if __name__ == '__main__':
    print(Solution().isInterleave("a", "", "a"))
    print('------')
    print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print('------')
    print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))
