# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        
        def leaf(rk):
            if rk==None:
                return []
            if rk.left ==None and rk.right==None :
                return [rk.val]
            else:
                return leaf(rk.left)+leaf(rk.right)
        if root1==None and root2==None:
            return True
        else:
            return leaf(root1)== leaf(root2)