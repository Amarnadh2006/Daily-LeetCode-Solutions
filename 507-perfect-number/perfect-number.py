class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        i=2
        j=num
        c=0
        while(i<=j):
            if num%i == 0:
                j = num/i
                if j<i:
                    break
                c+=i+j
                i+=1
            else:
                i+=1
        if c+1 == num:
            return True
        return False
            
        