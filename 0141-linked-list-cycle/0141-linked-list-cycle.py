# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        
        if slow and slow.next!=None:
            slow=slow.next
            fast=fast.next.next
        else:
            return False
        while fast and fast.next:
            if fast==slow:
                return True
            slow=slow.next
            fast=fast.next.next
        return False
        