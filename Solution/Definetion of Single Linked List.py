class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        return '{} -> {} '.format(self.val, repr(self.next))
    def append(self, val):
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)
    def delete(self, val):
        cur = self
        while cur:
            if cur.val == val:
                cur.val = cur.next.val
                cur.next = cur.next.next
            else:
                cur = cur.next
    def insert(self,index,val):
        cur = self
        nxt = self.next
        counter = 1
        if counter == index:
            tmp = Node(val)
            cur.next = tmp
            tmp.next = nxt
        else:
            counter += 1
            cur = nxt
            nxt = nxt.next

def reversed(root):
    pre = None
    cur = root
    while cur:
        post = cur.next
        cur.next = pre
        pre = cur
        cur = post
    root = pre
    return root

def list_append_listnode(lst):
    head = Node(0)
    for i in lst:
        head.append(i)
    return head.next

################################################
# Set up LinkedList
lst = [11,22,33]

head = cur = top = list_append_listnode(lst)
print()
print("input: {}".format(head))
# Delete Node

head.delete(22)
print("delete node: {}".format(head))
# Append Node at the end

head.append(22)
print("Append Node: {}".format(head))
# Insert Node

head.insert(1,22)
print("Insert Node: {}".format(head))
# reverse Node
head = reverse(head)
print("Reverse Node: {}".format(head))
print()
