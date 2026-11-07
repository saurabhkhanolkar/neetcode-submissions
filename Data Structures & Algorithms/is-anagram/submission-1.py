class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] in list(dict_s.keys()):
                dict_s[s[i]] =  dict_s[s[i]] + 1
            else:
                dict_s[s[i]] = 1
        for i in range(len(t)):
            if t[i] in list(dict_t.keys()):
                dict_t[t[i]] =  dict_t[t[i]] + 1
            else:
                dict_t[t[i]] = 1
    
        if dict_s == dict_t:
            return True
        else:
            return False
        

        