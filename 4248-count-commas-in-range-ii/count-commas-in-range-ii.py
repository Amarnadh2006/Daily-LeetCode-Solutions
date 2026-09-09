class Solution:
    def countCommas(self, n: int) -> int:
        count=0
        x=0
        if n<1000:
            return 0
        y=1000
        while(n-y>=0):
            count+=n-y
            y=y*1000
            x+=1
        return count+x