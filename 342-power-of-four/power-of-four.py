class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0 and n&(n-1) ==0 and len(bin(n))%2==1:
            return True
        return False
        
        