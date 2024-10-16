# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        q=deque()
        if not root:
            return []
        ans=[]
        q.appendleft(root)
        l=len(q)
        c=0
        while l!=0:
            
            la=[]
            for i in range(l):
                t=q.pop()
                la.append(t.val)
                if t.left:
                    q.appendleft(t.left)
                if t.right:
                    q.appendleft(t.right)
            if c==0:
                ans.append(la)
                c=1
            else:
                ans.append(la[::-1])
                c=0
                
            l=len(q)


        return ans

        