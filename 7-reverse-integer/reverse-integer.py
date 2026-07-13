class Solution(object):
    def reverse(self, x):
        sign = -1 if x<0 else 1
        c = 0
        x = abs(x)
        while(x>0):
            last = x%10
            c=c*10+last
            x = x//10
        if c < -2**31 or c > 2**31 - 1:
            return 0
        if sign == -1: return -c 
        else: return c
        