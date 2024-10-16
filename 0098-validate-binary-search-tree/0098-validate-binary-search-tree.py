# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid(rt,l,h):
            if not rt:
                return True
            if not (l<rt.val<h):
                return False
            return valid(rt.left,l,rt.val) and valid(rt.right,rt.val,h)
        return valid(root,float("-inf"),float("inf"))

        