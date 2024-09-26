# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        # if root==subRoot:
        #     # print(root.val,subroot.val)
        #     return True
        # elif root==None and subRoot!=None:
        #     # print(subRoot.val)
        #     return False
        # else:
        #     return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        if subRoot==None:
                return True
        elif root==None and subRoot!=None:
            return False
     
            
        def check(r,sr):
            if r==None and sr==None:
                return True
            elif r!=None and sr==None:
                return False
            elif r==None and sr!=None:
                return False
            if r.val==sr.val:
                return check(r.left,sr.left) and check(r.right,sr.right)
            else:
                return False
        
        ans=check(root,subRoot)

        return ans or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        