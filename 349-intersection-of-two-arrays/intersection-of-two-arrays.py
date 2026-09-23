class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=[]
        l1 = set(nums1)
        l2 = set(nums2)
        for x in l1:
            if x in l2:
                a.append(x)
        return a

        