class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''list1=[]
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
        '''
        list1=[]
        for i in range(len(s)):
            if s[i].isalnum()==1:
                list1.append(s[i].lower())
        print(list1)
        #str(list) doesnt convert list to string
        c=0
        for i in range(len(list1)):
            if list1[i] == list1[(len(list1)-1)-i]:
                c=c+1
            else:
                break
        if c == len(list1):
            return True
        else:
            return False
