# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        q=deque()
        q.appendleft(root)
        past=False
        while len(q)!=0:
            l=len(q)
            t=q.pop()
            if t==None:
                past=True
            else:
                if past==True:
                    return False
                q.appendleft(t.left)
                q.appendleft(t.right)
        return True