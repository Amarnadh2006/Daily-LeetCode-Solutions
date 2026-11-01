class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 1
        i=0
        for x in range(len(nums)):
            if nums[x]!=nums[i]:
                nums[i+1]=nums[x]
                i+=1
            
        return len(nums[:i+1:])



