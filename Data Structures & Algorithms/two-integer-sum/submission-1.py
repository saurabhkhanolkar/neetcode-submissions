class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    list1=[]
                    list1.append(i)
                    list1.append(j)
                    return list1 '''
        '''
        dic={}
        for i in range(len(nums)):
            dic[nums[i]] = target - nums[i]
        list1 = list(dic.keys())
        list2 = list(dic.values())

        for i in range(len(list1)):
            if (list1[i] in list2):
                if(list1[i]!=list2[i]):
                    list3 = []
                    list3.append(i)
        return list3
        '''
        mydic={}
        for i,n in enumerate(nums):
            mydic[n] = i
        key_list = list(mydic.keys())
        for i in range(len(key_list)):
            desired = target - key_list[i]
            if(((desired) in key_list) and (mydic[desired]!=i)):
                return([i,mydic[desired]])




        


        