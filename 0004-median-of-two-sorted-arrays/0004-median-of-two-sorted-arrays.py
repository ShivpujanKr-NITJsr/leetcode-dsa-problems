class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1=len(nums1)
        n2=len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        low=0
        high=n1
        left=(n1+n2+1)//2
        n=n1+n2
        while (low<=high):
            m1=low+(high-low)//2
            m2=left-m1
            l1=l2=float("-inf")
            r1=r2=float("inf")
            if m1<n1:
                r1=nums1[m1]
            if m2<n2:
                r2=nums2[m2]

            if m1-1>=0:
                l1=nums1[m1-1]
            if m2-1>=0:
                l2= nums2[m2-1]
            if l1<= r2 and l2 <=r1:
                if n%2==1:
                    return max(l1,l2)
                return (max(l1,l2)+min(r1,r2))/2.00
            elif l1>r2:
                high=m1-1
            else:
                low=m1+1
        return 0

        
        