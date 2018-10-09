# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        x = first = ListNode(0)
        while head:
            if head.val != val:
                x.next = ListNode(head.val)
                head = head.next
                x = x.next
            else:
                head = head.next
        
        return first.next