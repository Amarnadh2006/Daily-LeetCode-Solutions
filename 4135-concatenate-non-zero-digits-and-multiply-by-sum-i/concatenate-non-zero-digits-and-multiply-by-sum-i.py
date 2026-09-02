class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        s = ""
        sum =0
        for i in str(n):
            if i == "0":
                continue
            else:
                s+=i
                sum +=int(i)
        x = int(s)
        return x*sum



        