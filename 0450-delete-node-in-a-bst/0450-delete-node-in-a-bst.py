# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minVal(self,r):
        minv=r.val
        while r.left!=None:
            minv=r.left.val
            r=r.left
        return minv
    def deleteNode(self, root, key):
        if not root :
            return root
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        else:
            if root.left== None:
                return root.right
            elif root.right==None:
                return root.left
            
            root.val=self.minVal(root.right)
            root.right=self.deleteNode(root.right,root.val)
        return root

        