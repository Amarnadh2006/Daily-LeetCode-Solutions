class Solution(object):
    def isPalindrome(self, s):
        r = s.lower()
        for ch in r:
            if (97 <= ord(ch) <= 122) or (48 <= ord(ch) <= 57):
                continue
            else:
                r = r.replace(ch, "", 1)
        p = r[::-1]
        if r == p:
            return True
        else:
            return False