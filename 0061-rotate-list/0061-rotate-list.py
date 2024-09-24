# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        cur=head
        n=0
        while cur:
            cur=cur.next
            n+=1
        if n==0 or k==0 or k%n==0:
            return head
        k=k%n
        cur=head
        # print(k,n)
        while k!=0:
            cur=cur.next
            k-=1
        temp=head
        while cur and cur.next:
            cur=cur.next
            head=head.next
        
        t=head.next
        head.next=None
        cur.next=temp
        return t
        