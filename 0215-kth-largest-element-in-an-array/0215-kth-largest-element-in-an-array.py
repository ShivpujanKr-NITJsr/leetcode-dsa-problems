class Solution(object):
    def findKthLargest(self, nums, k):
        li=[]

        for i in nums:
            heapq.heappush(li,i)
            if len(li)>k:
                heapq.heappop(li)
        return heapq.heappop(li)
        