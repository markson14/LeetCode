# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        first = second = head
        res = collections.deque()
        while first:
            res.append(first.val)
            first = first.next
        res.rotate(k)
        while second:
            second.val = res.popleft()
            second = second.next
        return head