class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1=[]
        for i in range(len(s)):
            if s[i].isalnum()==1:
                list1.append(s[i])
        list2 = []
        for i in range(len(list1)-1,-1,-1):
            list2.append(list1[i])
        if str(list1).lower() == str(list2).lower():   #.lower() for case insensitive comparison 
            return True
        else: 
            return False
