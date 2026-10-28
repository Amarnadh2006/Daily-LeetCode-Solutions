class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        a = m + n - 1
        b = n - 1
        c = m - 1

        while b >= 0 and c >= 0:
            if nums2[b] >= nums1[c]:
                nums1[a] = nums2[b]
                b -= 1
            else:
                nums1[a] = nums1[c]
                c -= 1
            a -= 1

        while b >= 0:
            nums1[a] = nums2[b]
            a -= 1
            b -= 1