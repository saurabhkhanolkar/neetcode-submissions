class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        def func(x):
            return x[1]
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] =  dic[nums[i]] + 1 
            else:
                dic[nums[i]] = 1
        sorted_dic = dict(sorted(dic.items(), key = func, reverse = True))
        listx=[]
        for i in range(k):
            listx.append(list(sorted_dic.keys())[i])
        return listx


        
            
        