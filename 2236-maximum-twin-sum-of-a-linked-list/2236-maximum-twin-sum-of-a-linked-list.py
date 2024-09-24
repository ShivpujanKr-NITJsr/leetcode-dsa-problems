# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        def reverse(self,h):
            prev=None
            while h:
                temp=h.next
                h.next=prev
                prev=h
                h=temp
            return prev
        slow=head
        fast=head
        
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        rev=reverse(self,slow.next)
        # print(rev)

        maxi=rev.val+head.val

        # mid=slow
        slow.next=None
        slow=head
    
        while slow:
            v=slow.val+rev.val
            if v>maxi:
                maxi=v
            
            slow=slow.next
            rev=rev.next

        return maxi
        
        