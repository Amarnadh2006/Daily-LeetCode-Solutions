class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        csum = msum = sum(nums[:k])
        for x in range(0,len(nums)-k):
            csum = csum-nums[x]+nums[x+k]
            if csum>msum:
                msum=csum
        return round(msum/k ,5)
        