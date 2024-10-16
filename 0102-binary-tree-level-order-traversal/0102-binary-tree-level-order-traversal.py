# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        q=deque()
        if not root:
            return []
        q.appendleft(root)
        ans=[]
        l=len(q)
        while len(q)!=0:
            l=len(q)
            li=[]
            for i in range(l):
                t=q.pop()
                li.append(t.val)
                if t.left:
                    q.appendleft(t.left)
                if t.right:
                    q.appendleft(t.right)
            ans.append(li)
        return ans
                
        