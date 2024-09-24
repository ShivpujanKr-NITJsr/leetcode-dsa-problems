# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        cur=head
        last=head

        while n!=0:
            last=last.next
            n-=1
        if last==None:
            return head.next
        while last.next:
            last=last.next
            cur=cur.next
        cur.next=cur.next.next
        return head

        