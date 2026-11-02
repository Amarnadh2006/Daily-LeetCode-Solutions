class Solution:
    def maxArea(self, height: list[int]) -> int:
        f,l = 0,len(height)-1
        tot =0
        while f<l:
            if height[f]<=height[l]:
                temp = height[f]*(l-f)
                f+=1
            else:
                temp = height[l]*(l-f)
                l-=1
            if temp>tot:
                tot = temp
        return tot

        