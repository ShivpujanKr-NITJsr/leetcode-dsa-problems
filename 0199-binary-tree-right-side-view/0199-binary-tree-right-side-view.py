# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        levels=[]

        def rightSide(node,level):
            if not node:
                return
            if len(levels)==level:
                levels.append([]) 
            rightSide(node.left,level+1)
            levels[level].append(node.val)
            rightSide(node.right,level+1)
        rightSide(root,0)
        ans=[]
        for i in range(len(levels)):
            l=len(levels[i])
            # print(levels[i])
            ans.append(levels[i][l-1])
        return ans
        