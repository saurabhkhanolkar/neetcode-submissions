class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in range(len(nums)):
            if nums[i] in list(dic.keys()):
                dic[nums[i]] = dic[nums[i]] + 1
            else:
                dic[nums[i]] = 1
        print(dic)
        list_values = list(dic.values())
        for i in range(len(list_values)):
            if list_values[i]>1:
                return True
        
        return False
                

         






