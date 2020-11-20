#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummyhead = ListNode(0)
        dummyhead.next = head
        cur = head.next
        lastordered = head
        while cur:
            if lastordered.val <= cur.val:
                lastordered = lastordered.next
            else:
                prev = dummyhead
                while prev.next.val <= cur.val:
                    prev = prev.next
                '''
                链表节点交换
                1. 去掉当前节点，使前一个节点连接在后一个节点上
                2. 当前节点衔接到前两个节点的next上
                3. 前两个节点的next为当前节点
                '''
                lastordered.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastordered.next
        return dummyhead.next

# @lc code=end
