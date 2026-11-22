class Solution:
    def checkString(self, s: str) -> bool:
        seen = 0
        for x in s:
            if x == 'a':
                if seen==1:
                    return False
            if x == 'b':
                seen = 1
        return True
        