#
# @lc app=leetcode.cn id=1657 lang=python3
#
# [1657] 确定两个字符串是否接近
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 距离不相等
        if len(word1) != len(word2):
            return False
        c1 = [0] * 26
        c2 = [0] * 26

        # 记录位置信息
        for w in word1:
            c1[ord(w)- ord('a')] += 1
        for w in word2:
            c2[ord(w)- ord('a')] += 1

        # 若仅有字母仅存在其中一个list中，则False
        for i,j in zip(c1, c2):
            if (i == 0 and j != 0) or (i != 0 and j == 0):
                return False
        
        # 返回排序后是否相等，可以看出是否能够进行字母替换
        return sorted(c1) == sorted(c2)
        
        

        
# @lc code=end

