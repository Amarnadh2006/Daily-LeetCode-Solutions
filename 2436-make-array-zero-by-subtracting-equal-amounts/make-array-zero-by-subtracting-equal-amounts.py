class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sets = set(nums)
        if 0 in sets:
            sets.remove(0)
        return len(sets)
        