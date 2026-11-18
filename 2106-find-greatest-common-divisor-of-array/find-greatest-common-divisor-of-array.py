class Solution:
    def findGCD(self, nums: list[int]) -> int:
        def hcf(m,n):
            f = m%n
            if f==0:
                return n
            else:
                return hcf(n,f)

        return hcf(max(nums),min(nums))
        