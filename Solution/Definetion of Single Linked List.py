class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Set up LinkedList
node1 = Node(11)
node2 = Node(22)
node3 = Node(33)
node1.next = node2
node2.next = node3

head = cur = top = node1
out = []
res = []

# print input linkedlist
while head:
    out.append(head.val)
    print(bool(head.next))
    head = head.next
    

# Delete Node
while cur:
    if cur.val == 22:
        cur.val = cur.next.val
        cur.next = cur.next.next
    else:
        cur = cur.next

# print output linkedlist
while top:
    res.append(top.val)
    top = top.next

print("input: {}".format(out))
print("output: {}".format(res))
