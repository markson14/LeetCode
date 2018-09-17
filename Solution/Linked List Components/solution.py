# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        res = 0
        setg = set(G)
        while head:
            if head.val in setg and (head.next == None or head.next.val not in setg):
                res +=1
            head = head.next
        return res