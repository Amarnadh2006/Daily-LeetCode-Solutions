class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        a=[]
        for x in range(len(nums)//2):
            small = min(nums)
            nums.remove(small)
            big = max(nums)
            nums.remove(big)
            av = (small+big)/2
            a.append(av)
        return min(a)
        


