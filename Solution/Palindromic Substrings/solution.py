class Solution:
    def countSubstrings(self, s): # 700ms 暴力
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count

    def countSubstrings(self, s):  # 170ms 中心展开法
            """
            :type s: str
            :rtype: int
            """
            n = len(s)
            count = 0
            for center in range(2*n - 1):
                left = center // 2
                right = left + center % 2
                # print(left,right)
                while left >= 0 and right < n and s[left] == s[right]:
                    # print(left,right)
                    count += 1
                    left -= 1
                    right += 1
            return count 