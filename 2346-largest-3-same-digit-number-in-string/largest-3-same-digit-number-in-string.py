class Solution:
    def largestGoodInteger(self, num: str) -> str:
        visited = 0
        t="0"
        for x in range(0,len(num)-2):
            if num[x:x+3:] == num[x]*3:
                visited = 1
                if int(num[x])>int(t):
                    t = num[x]
        if visited == 0:
            return ""
        else:
            return t*3

                
        