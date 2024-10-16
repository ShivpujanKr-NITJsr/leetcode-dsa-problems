# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        d={}
        ans=[]
        def same(rt):
            if rt==None:
                return "N"
            else:
                k= str(rt.val)+","+same(rt.left)+","+same(rt.right)
                if k in d:
                    if d[k]==1:
                        d[k]+=1
                        ans.append(rt)
                else:
                    d[k]=1
                return k
        same(root)
        return ans
        