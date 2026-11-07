class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        new = set(nums)
        n = len(nums)
        for x in new:
            a= nums.count(x)
            if a>(n/2):
                return x
        