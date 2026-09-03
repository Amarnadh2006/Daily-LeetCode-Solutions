class Solution:
    def totalMoney(self, n: int) -> int:
        a=n//7
        d=a
        b=4
        sum=0
        while(a>0):
            sum+=7*b
            b+=1
            a-=1
        c=n%7
        e=d+1
        while(c>0):
            sum+=e
            e+=1
            c-=1
        return sum


            
            

        