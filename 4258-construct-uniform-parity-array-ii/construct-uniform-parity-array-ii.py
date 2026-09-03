class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        o=0
        for j in nums1:
            if j%2!=0:
                o+=1
                break
        if min(nums1)%2==0 and o==1:
            return False
        return True
