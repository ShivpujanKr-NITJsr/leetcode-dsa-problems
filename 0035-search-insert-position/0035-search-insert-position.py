class Solution(object):
    def searchInsert(self, nums, target):
        l=0
        h=len(nums)-1

        while l<=h:
            m=l+(h-l)//2

            if nums[m]>target:
                h=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m

        return l
        