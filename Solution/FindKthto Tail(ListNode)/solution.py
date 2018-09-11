class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        
        # 设置两个指针，先让p2走 k-1个。然后p1,p2一起走完剩下的，p1即为所求
        p1 = head
        p2 = head
        while k > 1:
            if p2.next != None:
                p2 = p2.next
                k-=1
            else:
                return None
        while p2.next != None:
            p2 = p2.next
            p1 = p1.next
        return p1