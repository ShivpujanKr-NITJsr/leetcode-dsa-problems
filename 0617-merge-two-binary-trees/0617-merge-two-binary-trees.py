# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        if root1==None and root2==None:
            return None
        if root1==None or root2==None:
            return root1 if not root2 else root2
        root1.val=root1.val+root2.val
        root1.left=self.mergeTrees(root1.left,root2.left)
        root1.right=self.mergeTrees(root1.right,root2.right)

        return root1

        