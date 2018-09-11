class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in array:
            if target in i:
                return True
        return False