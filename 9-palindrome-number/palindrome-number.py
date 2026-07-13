class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        y = len(x)
        for a in range(y // 2):
            if x[a] != x[y - a - 1]:
                return False
        return True