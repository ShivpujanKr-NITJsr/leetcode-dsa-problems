class Solution(object):
    def reverse(self, x):
        maxi=2**31- 1
        mini=-2**31

        ans=0
        sign =-1 if x<0 else 1

        x=abs(x)

        while x!=0:
            if ans>maxi/10 or ans <mini/10:
                return 0
            d=x%10
            ans=ans*10 +d
            x=x//10

        ans=ans*sign

        if ans>maxi or ans <mini:
            return 0
        return ans

        