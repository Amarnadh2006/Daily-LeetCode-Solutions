class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        s=0
        m=1
        while(n>0):
            x = n%10
            s+=x
            m*=x
            n=n//10
        if temp % (m+s)==0:
            return True
        return False
        
        