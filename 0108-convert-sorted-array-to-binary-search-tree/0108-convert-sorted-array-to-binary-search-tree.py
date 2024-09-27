# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def bst(nums,left,right):
            if left>right:
                return None
            m=left+(right-left)//2
            tn=TreeNode(nums[m])
            tn.left=bst(nums,left,m-1)
            tn.right=bst(nums,m+1,right)
            return tn
        if len(nums)==0:
            return None
        return bst(nums,0,len(nums)-1)
        