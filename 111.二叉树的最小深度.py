#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque()
        visited = set()
        queue.append(root)
        # root 本身就是一层，depth 初始化为 1
        depth = 1
        while queue:
            # 将当前队列中的所有节点向四周扩散
            for i in range(len(queue)):
                node = queue.popleft()
                # 判断是否到达终点
                if not node.left and not node.right:
                    return depth
                # 将 cur 的相邻节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 这里增加步数
            depth += 1
        return depth
            
# @lc code=end

