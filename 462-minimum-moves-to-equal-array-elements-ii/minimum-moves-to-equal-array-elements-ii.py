class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        total = 0
        temp = nums[n//2]
        for x in nums:
            total+=abs((temp)-(x))
        return total
        