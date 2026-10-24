class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        final = ""
        if sum>9*num:
            return ""
        for x in range(num):
            if sum==0:
                final+=(num-len(final))*"0"
                break
            elif sum>=9:
                sum-=9
                final+="9"
            elif sum<9:
                final+=str(sum)
                sum=0
        return final
            

        