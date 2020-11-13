#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = [root]
        if not root: return []
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if i == 0: res.append(cur.val)
                if cur.right: q.append(cur.right)
                if cur.left: q.append(cur.left)

        return res
# @lc code=end

