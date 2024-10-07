# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        def path(rt,rk):
            if rt==None:
                return []
            if rt==rk:
                return [rt]
            else:
                left_path= path(rt.left, rk)
                if left_path:
                    return [rt]+left_path
                right_path =path(rt.right,rk)
                if right_path:
                    return [rt]+right_path
                return []

        a=path(root,p)
        b=path(root,q)
        i=0
        j=0
        li=len(a)
        lj=len(b)
        ans=None
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                lca = a[i]  # Update LCA to the last matching node
            else:
                break
            i += 1
            j += 1
        
        return lca

                

        