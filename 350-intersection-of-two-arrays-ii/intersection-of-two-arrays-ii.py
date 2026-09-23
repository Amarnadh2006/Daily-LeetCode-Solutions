class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=[]
        for x in nums1:
            if x in nums2:
                a.append(x)
                nums2.remove(x)
        return a
        