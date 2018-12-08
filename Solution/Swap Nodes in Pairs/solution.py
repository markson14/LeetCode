# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        one = []
        two = []
        cur = top = head
        while top:
            one.append(top.val)
            top = top.next
            if top:
                two.append(top.val)
                top = top.next
        while cur:
            if two:
                cur.val = two.pop(0)
                cur = cur.next
            if one:
                cur.val = one.pop(0)
                cur = cur.next
        return head

class Solution2:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        直接内部交换，没有适用外部空间
        """
        tag = 1
        if head and head.next:
            fast = head.next
            slow = head
        else:
            return head
        while fast:
            if tag:
                fast.val,slow.val = slow.val,fast.val
                fast = fast.next
                slow = slow.next
                tag -= 1
            else:
                fast = fast.next
                slow = slow.next
                tag += 1
        return head