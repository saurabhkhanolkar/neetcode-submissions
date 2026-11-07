class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def allsame(strs):
            for i in range(len(strs)):
                if strs[i] != strs[0]:
                    return 0
            return 1

            
        if (allsame(strs) == 1):
            return[strs]


        
        def isanagram(a,b):
            dic1 = {}
            dic2 = {}
            for i in range(len(a)):
                if a[i] in dic1:
                    dic1[a[i]] = dic1[a[i]] + 1
                else:
                    dic1[a[i]] = 1 
            
            for i in range(len(b)):
                if b[i] in dic2:
                    dic2[b[i]] = dic2[b[i]] + 1
                else:
                    dic2[b[i]] = 1 
            
            if dic1 == dic2:
                return 1 
            else: 
                return 0 


        isprocessed = [] 
        list2 = []
        for i in range(len(strs)):
            list1 = []
            if strs[i] in isprocessed:
                continue
            for j in range(i+1, len(strs)):
                if strs[j] in isprocessed:
                    continue
                if isanagram(strs[i],strs[j]) == 1:
                    isprocessed.append(strs[j])
                    list1.append(strs[j])
            list1.append(strs[i])
            list2.append(list1)
            isprocessed.append(strs[i])
        return list2 
           
        
            
                    

        
        