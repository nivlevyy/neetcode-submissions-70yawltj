class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        if not prices or length<2:
            return 0
    
        start=0
        end=1
        maxi=0
        while end < length:
            
            if prices[start]>prices[end]:
                start=end
            else:
                maxi=max(maxi,prices[end]-prices[start])
            end+=1
        return maxi




            

        