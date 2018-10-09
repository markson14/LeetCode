class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
node1 = Node(32)
node2 = Node(83)
node3 = Node(11)
node1.next = node2
node2.next = node3

head = node1
out = []
while head:
    out.append(head.val)
    head = head.next
print(out)