class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in list(dic.keys()):
                dic[nums[i]]=dic[nums[i]]+1
            else:
                dic[nums[i]] = 1
        for i in list(dic.values()):
            if i != 1:
                return True
        return False


         






