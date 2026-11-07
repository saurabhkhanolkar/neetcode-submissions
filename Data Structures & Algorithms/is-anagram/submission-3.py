class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}
        dictionary2 = {}
        for i  in range(len(s)):
            if s[i] in dictionary1:
                dictionary1[s[i]] = dictionary1[s[i]] + 1
            else:
                dictionary1[s[i]] = 1 
        for i  in range(len(t)):
            if t[i] in dictionary2:
                dictionary2[t[i]] = dictionary2[t[i]] + 1
            else:
                dictionary2[t[i]] = 1 
        if dictionary1 == dictionary2:
            return True
        else:
            return False



        