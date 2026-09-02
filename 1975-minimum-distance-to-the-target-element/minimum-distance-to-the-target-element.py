class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        a = len(nums)+start
        for i in range(len(nums)):
            if (nums[i]==target):
                if abs(i - start)<a:
                    a = abs(i-start)
        return a
                
        