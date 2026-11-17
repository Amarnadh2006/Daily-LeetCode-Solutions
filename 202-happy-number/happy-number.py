class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            if n<=10:
                if n==1 or n==7 or n==10:
                    return True
                else:
                    return False
            else:
                s=0
                while(n>0):
                    temp = n%10
                    s += temp*temp
                    n=n//10
                n = s
                return happy(n)
        return happy(n)
            
        