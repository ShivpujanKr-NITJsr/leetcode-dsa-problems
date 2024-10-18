# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        
        
        if not head or not head.next:
            return head
        odd =head
        even=evenh=head.next

        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next

        odd.next=evenh
        return head
        