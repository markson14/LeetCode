# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: # scan twice, first time to get the length.
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        top = head
        x = ListNode(0)
        x.next = head
        length = 0
        while top:
            length += 1
            top = top.next
        count = length - n
        top = x
        while count:
            count -= 1
            top = top.next
        top.next = top.next.next
        return x.next

class Solution2: # using two pointer which is even fast, only scan once
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head