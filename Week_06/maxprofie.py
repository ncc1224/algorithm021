class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:return 0
        res=0
        start=end=prices[0]
        for p in prices[1:]:
            if p<=end:
                res += end-start
                start=end=p
            else:
                end=p
        res += end-start
        return res
class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                res +=  prices[i+1]-prices[i]
        return res
class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        prices.append(0)
        stack=[]
        for i in range(len(prices)):
            if stack and prices[i]<=stack[-1]:
                res+=stack[-1]-stack[0]
                stack=[]
            stack.append(prices[i])
        return res
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        prices.append(0)
        start,end=prices[0],prices[0]
        for i in range(1,len(prices)):
            if prices[i]<=prices[i-1]:
                res+=end-start
                start=prices[i]
            end = prices[i]
        return res










        
