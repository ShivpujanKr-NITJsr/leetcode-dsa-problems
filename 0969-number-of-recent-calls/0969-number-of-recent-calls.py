class RecentCounter(object):

    def __init__(self):
        self.c=[]

    def ping(self, t):
        l=t-3000
        h=t
        a=0
        self.c.append(t)
        for i in range(len(self.c)-1,-1,-1):
            if self.c[i]<=h and self.c[i]>=l:
                a+=1
            else:
                return a
        return a
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)