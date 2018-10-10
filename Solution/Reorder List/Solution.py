# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        res = []
        first = head
        while first:
            res.append(first.val)
            first = first.next
        reorder = []
        while res:
            reorder.append(res.pop(0))
            if res:
                reorder.append(res.pop(-1))
        
        while head:
            head.val = reorder.pop(0)
            head = head.next
            