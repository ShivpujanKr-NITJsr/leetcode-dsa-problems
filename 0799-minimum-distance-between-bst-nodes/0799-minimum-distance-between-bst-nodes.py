# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        ans=float("inf")

        def inorder(node):
            if node==None:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        arr=inorder(root)

        for i in range(1,len(arr)):
            k=arr[i]-arr[i-1]
            ans=ans if ans<k else k
        return ans


        
        