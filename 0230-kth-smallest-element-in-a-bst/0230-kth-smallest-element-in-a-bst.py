# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        def inorder(rt):
            if not rt:
                return []
            return inorder(rt.left)+[rt.val]+inorder(rt.right)
        s=inorder(root)
        return s[k-1]
        