# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.dia=0
        def depthOf(rl):
            if rl==None:
                return 0
            o=depthOf(rl.left)
            k=depthOf(rl.right)
            self.dia=max(self.dia,o+k)
            return o+1 if o>k else k+1

        depthOf(root)
        return self.dia


        

        