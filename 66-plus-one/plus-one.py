class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a=""
        sol=[]
        for x in digits:
            a+=str(x)
        b=int(a)
        b+=1
        a=str(b)
        for y in a:
            sol.append(int(y))
        return sol



        