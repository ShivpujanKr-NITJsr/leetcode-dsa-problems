# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root==None:
            return root
        lef=self.invertTree(root.left)
        rig=self.invertTree(root.right)
        root.left=rig
        root.right=lef
        return root
        