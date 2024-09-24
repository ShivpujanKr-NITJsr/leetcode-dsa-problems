# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if root==None :
            return []
        if (root.left==None ):
            k= [root.val]
            return k+self.inorderTraversal(root.right)
        else:
            k= [root.val]
            return self.inorderTraversal(root.left)+k+self.inorderTraversal(root.right)
        



        