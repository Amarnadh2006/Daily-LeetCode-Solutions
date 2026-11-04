class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s=sum(nums)
        tot=0
        for x in range(len(nums)):
            tot+=nums[x]
            if tot-nums[x]==(s-nums[x])/2:
                return x
        return -1
            

