class Solution(object):
    def findDuplicate(self, nums):
        for i in range(len(nums)):

            absnum=abs(nums[i])

            if(nums[absnum]<0):
                return absnum
            else:
                nums[absnum]=-nums[absnum]

        return -1

        
        

        