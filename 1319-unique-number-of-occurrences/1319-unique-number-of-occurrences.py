class Solution(object):
    def uniqueOccurrences(self, arr):
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s={}
        for i in d.values():
            if i in s:
                return False
            else:
                s[i]=1
        return True
        