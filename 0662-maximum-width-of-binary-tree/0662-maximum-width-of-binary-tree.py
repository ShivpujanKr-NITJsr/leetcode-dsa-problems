# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        I=0
        q=deque()
        ans=0
        q.appendleft([root,0])
        while len(q)!=0:
            l=len(q)
            f=0
            la=-1
            
            for i in range(l):
                t=q.pop()
                if i==0:
                    f=t[1]
                if i==l-1:
                    la=t[1]
                if t[0].left:
                    q.appendleft([t[0].left,t[1]*2+1])
                if t[0].right:
                    q.appendleft([t[0].right,t[1]*2+2])
            ans=max(ans,la-f+1)
        return ans

            

        