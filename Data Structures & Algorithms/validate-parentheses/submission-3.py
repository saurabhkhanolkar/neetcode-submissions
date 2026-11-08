class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        for i in range(len(s)):
            if s[i] in ('(' , '{', '[' ):
                list1.append(s[i])
            elif s[i] in (')' , '}', ']' ):
                if len(list1) == 0:
                    return False
                a = list1.pop()
                if a == '(' and s[i] != ')':
                    return False
                elif a == '{' and s[i] != '}':
                    return False
                elif a == '[' and s[i] != ']':
                    return False
        if len(list1) != 0:
            return False 
        else:
            return True

        