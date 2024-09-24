# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        
        fir=head
        sec=head.next

        tem=sec.next
        fir.next=tem
        sec.next=fir
        head=sec

        while fir.next and fir.next.next :
            tem=fir.next
            tem2=fir.next.next.next
            fir.next=fir.next.next
            fir.next.next=tem
            tem.next=tem2
            fir=fir.next.next
        return head
            

            
        