# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        cur=head
        a=[]
        while cur:
            t=cur.next
            if cur.val<x:
                a.append(cur)

            cur=t
            
        if len(a)==0:
            return head
        m=a[0]
        l=len(a)
        while head and head.val<x:
            
            head=head.next
        temp=head
        while head and head.next:
            if head.next.val<x:
                head.next=head.next.next
            else:
                head=head.next
        for i in range(1,l):
            a[i-1].next=a[i]
        
        a[l-1].next=temp
        
        return m
        