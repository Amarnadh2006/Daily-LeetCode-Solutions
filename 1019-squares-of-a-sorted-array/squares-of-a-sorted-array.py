class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for x in range(len(nums)):
            nums[x]=abs(nums[x]**2)
        return sorted(nums)
        