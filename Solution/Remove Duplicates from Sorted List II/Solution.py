# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = []
        b = []
        first = head
        while first:
            if not first.val in a and not first.val in b:
                a.append(first.val)
                first = first.next
            else:
                if not first.val in b:
                    a.remove(first.val)
                    b.append(first.val)
                    first = first.next
                else:
                    first = first.next
        dummy = h1 = ListNode(0)
        while a:
            dummy.next = ListNode(a.pop(0))
            dummy = dummy.next
        return h1.next