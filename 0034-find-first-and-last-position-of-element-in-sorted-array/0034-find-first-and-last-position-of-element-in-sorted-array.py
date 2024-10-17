class Solution(object):
    def searchRange(self, nums, target):
        f=-1
        l=-1

        low=0
        h=len(nums)-1

        while low<=h:
            m=low+(h-low)//2
            if nums[m]>target:
                h=m-1
            elif nums[m]<target:
                low=m+1
            else:
                l=m
                low=m+1
        low=0
        h=len(nums)-1

        while low<=h:
            m=low+(h-low)//2
            if nums[m]>target:
                h=m-1
            elif nums[m]<target:
                low=m+1
            else:
                f=m
                h=m-1
        return [f,l]