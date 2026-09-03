class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        o=0
        e=0
        for i in nums1:
            if i%2==0:
                e+=1
                break
        for j in nums1:
            if j%2!=0:
                o+=1
                break
        if min(nums1)%2==0 and o==1:
            return False
        return True
