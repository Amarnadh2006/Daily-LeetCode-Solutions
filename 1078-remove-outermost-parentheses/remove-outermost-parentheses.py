class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        final = ""
        for x in s:
            if x=="(" and c==0:
                c+=1
                continue
            elif x=="(":
                c+=1
                final+="("
            elif x==")" and c==1:
                c-=1
                continue
            elif x==")":
                c-=1
                final+=")"
        return final
        