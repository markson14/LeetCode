#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def __init__(self):
        self.mp = defaultdict(int)
        self.res = set()

    def serials(self,root):
        if not root:
            return '#'
        left = self.serials(root.left)
        right = self.serials(root.right)
        final = '{},{},{}'.format(root.val,left,right)
        return final

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return None
        left = self.findDuplicateSubtrees(root.left)
        right = self.findDuplicateSubtrees(root.right)
        ss = self.serials(root)
        self.mp[ss] += 1
        if self.mp[ss] == 2:
            self.res.add(root)
        # print(self.mp)
        return self.res
# @lc code=end

