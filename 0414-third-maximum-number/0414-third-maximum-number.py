class Solution(object):
    def thirdMax(self, nums):
        max1=float("-inf") 
        max2=float("-inf")   
        
        max3=float("-inf")   
        
        for num in nums:
            if num>max1:
                max3 =max2
                max2= max1
                max1=num
            elif max1 >num and num>max2:
                max3=max2
                max2=num
            elif max2>num and num>max3:
                max3=num

        return max1 if max3 == float("-inf")  else max3
        