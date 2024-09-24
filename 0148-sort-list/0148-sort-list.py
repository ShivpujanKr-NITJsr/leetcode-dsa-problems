# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        
        a=[]

        if head==None or head.next==None:
            return head

        cur=head
        while cur:
            a.append(cur)
            cur=cur.next

        a.sort(key=lambda x:x.val)

        ans=ListNode()
        head=ans
        
        for i in range(1,len(a)):
            a[i-1].next=a[i]
            if i==len(a)-1:
                a[i].next=None
        
        return a[0]
        