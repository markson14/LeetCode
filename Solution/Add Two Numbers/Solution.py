# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        cur = res
        bit = 0
        while l1 != None or l2 != None:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            tmp = x + y + bit
            bit = tmp // 10
            cur.next = ListNode(tmp%10)
            cur = cur.next
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        if bit > 0:
            cur.next = ListNode(bit)
        return res.next