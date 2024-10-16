# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        
        def sym(rl,rr):
            if rl==None and rr==None:
                return True
            if rl==None or rr==None:
                return False
            if rl.val!=rr.val:
                return False
            return sym(rl.left,rr.right) and sym(rl.right,rr.left)

        return sym(root.left,root.right)
        