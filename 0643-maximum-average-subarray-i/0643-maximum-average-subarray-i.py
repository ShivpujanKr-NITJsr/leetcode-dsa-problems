class Solution(object):
    def findMaxAverage(self, nums, k):
        
        s=0.00000

        for i in range(k):
            s+=nums[i]

        ans=0.00000
        ans=s/k
        for i in range(k,len(nums)):
            s+=nums[i]
            s-=nums[i-k]
            ans=max(ans,s/k)
        return ans
        