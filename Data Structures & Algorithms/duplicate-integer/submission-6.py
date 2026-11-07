class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list2 = []
        for i in range(len(nums)):
            if nums[i] in list2:
                return True
            list2.append(nums[i])
        return False