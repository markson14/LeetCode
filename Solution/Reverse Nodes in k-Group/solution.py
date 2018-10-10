# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res = []
        cur = first = head
        c = k
        tmp = collections.deque()
        while cur:
            if c:
                c -= 1
                tmp.appendleft(cur.val)
                cur = cur.next
            else:
                c = k
                res.extend(tmp)
                tmp = collections.deque()
        if not c:
            res.extend(tmp)
        while res:
            first.val = res.pop(0)
            first = first.next
        return head
        
            