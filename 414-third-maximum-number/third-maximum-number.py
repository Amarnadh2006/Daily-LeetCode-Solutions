class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        n = len(nums)
        if n>=3:
            return nums[-3]
        else:
            return nums[-1]

            

        