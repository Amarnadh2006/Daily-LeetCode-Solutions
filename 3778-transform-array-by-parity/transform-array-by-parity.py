class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        c=0
        for _ in nums:
            if _%2 == 0:
                c+=1
        final = [0]*c
        final+=[1]*(len(nums)-c)
        return final
        