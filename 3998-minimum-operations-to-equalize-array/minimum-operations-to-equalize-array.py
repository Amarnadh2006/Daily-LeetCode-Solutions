class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sets = set(nums)
        if len(sets) == 1:
            return 0
        else:
            return 1
        