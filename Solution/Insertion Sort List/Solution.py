# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        x = k = ListNode(0)
        while head:
            res.append(head.val)
            head = head.next
        res = sorted(res,reverse = True)
        while res:
            x.next = ListNode(res.pop())
            x = x.next
        return k.next