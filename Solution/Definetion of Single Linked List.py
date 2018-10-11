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

def list_append_listnode(lst):
    head = Node(0)
    for i in lst:
        head.append(i)
    return head.next

# Set up LinkedList
lst = [11,22,33]

head = cur = top = list_append_listnode(lst)
print()
print("input: {}".format(head))
# Delete Node
while cur:
    if cur.val == 22:
        cur.val = cur.next.val
        cur.next = cur.next.next
    else:
        cur = cur.next

# print output linkedlist

print("output: {}".format(head))
print()
