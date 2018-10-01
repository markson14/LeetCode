# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node = []
        head = p = ListNode(0)
        
        for l in lists:
            while l:
                node.append(l.val)
                l = l.next
        for i in sorted(node):
            p.next = ListNode(i)
            p = p.next
        return head.next