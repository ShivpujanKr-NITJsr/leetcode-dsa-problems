# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        h=ListNode()
        ans=h
        while l1 and l2:
            v=l1.val+l2.val+carry
            carry=v//10
            v=v%10
            t=ListNode(v)
            h.next=t
            h=h.next
            l1=l1.next
            l2=l2.next
        while l1:
            v=l1.val+carry
            carry=v//10
            v=v%10
            t=ListNode(v)
            h.next=t
            h=h.next
            l1=l1.next
        while l2:
            v=l2.val+carry
            carry=v//10
            v=v%10
            t=ListNode(v)
            h.next=t
            h=h.next
            l2=l2.next
        if carry==1:
            t=ListNode(1)
            h.next=t
           
        return ans.next