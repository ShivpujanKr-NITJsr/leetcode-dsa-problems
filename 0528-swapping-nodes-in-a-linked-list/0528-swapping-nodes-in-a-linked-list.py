# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        n=k
        cur=head

        prev=cur
        while k!=0:
            prev=cur
            cur=cur.next
            k-=1
        temp=head
        if cur==None:
            t=prev.val
            prev.val=head.val
            head.val=t
            return head
        while cur.next:
            
            cur=cur.next
            temp=temp.next
        fir=head
        
        while n!=1:
            fir=fir.next
            n-=1
        t=fir.val
        fir.val=temp.next.val
        temp.next.val=t
        return head

        
        