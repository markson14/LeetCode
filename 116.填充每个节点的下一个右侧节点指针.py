#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect_two_node(self, node1, node2):
        if not node1 or not node2:
            return
        node1.next = node2
        self.connect_two_node(node1.left, node1.right)
        self.connect_two_node(node2.left, node2.right)
        self.connect_two_node(node1.right, node2.left)

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        self.connect_two_node(root.left, root.right)
        return root
        
# @lc code=end

