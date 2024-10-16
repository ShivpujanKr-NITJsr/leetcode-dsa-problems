class Solution(object):
    def largestAltitude(self, gain):
        s=0
        ans=0
        for i in gain:
            s+=i
            ans=max(ans,s)

        return ans
        