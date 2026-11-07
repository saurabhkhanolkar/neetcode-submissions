class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list_new = []
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    list_new.append(prices[j] - prices[i]) 
        if len(list_new) != 0:
            return(max(list_new))
        else:
            return 0

        
        