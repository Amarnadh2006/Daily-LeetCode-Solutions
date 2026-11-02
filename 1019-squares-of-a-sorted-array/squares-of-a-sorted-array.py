class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        f = 0
        l = len(nums)-1
        n = []
        for x in range(len(nums)):
            if abs(nums[f])>=abs(nums[l]):
                n.append(abs(nums[f]**2))
                f+=1
            else:
                n.append(abs(nums[l]**2))
                l-=1
        return n[::-1]
