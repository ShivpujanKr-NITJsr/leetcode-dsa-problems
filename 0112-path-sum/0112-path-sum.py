# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root==None:
            return False
        if root.left==None and root.right==None:
            if root.val==targetSum:
                return True
            return False
        else:
            if root.left==None:
                return self.hasPathSum(root.right,targetSum-root.val)
            elif root.right==None:
                return self.hasPathSum(root.left,targetSum-root.val)
            else:
                return self.hasPathSum(root.right,targetSum-root.val) or self.hasPathSum(root.left,targetSum-root.val)


        