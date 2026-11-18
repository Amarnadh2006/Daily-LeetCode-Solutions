class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(c**(1/2))
        i=0
        while(i<=n):
            t = (i*i)+(n*n)
            if t==c:
                return True
            elif t<c:
                i+=1
            elif t>c:
                n-=1
        return False
