class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n= set(nums)
        s=[]
        for x in range(1,len(nums)+1):
            if x not in n:
                s.append(x)
        return s

        