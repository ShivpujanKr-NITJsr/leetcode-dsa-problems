# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        
        def good(r,v):
            if r==None:
                return 0
            count=1 if r.val>=v else 0

            
            v= max(v,r.val)

            
            count +=good(r.left,v)
            count+=good(r.right,v)

            return count
            

        return good(root,root.val)
       