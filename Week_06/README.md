股票问题IV
class Solution:
    def maxProfit0(self, k: int, prices: List[int]) -> int:
        if not k or len(prices)<2:return 0
        n=len(prices)
        k=min(k,n//2)
        buy,sell=[[0]*(k+1) for i in range(n)],[[0]*(k+1) for i in range(n)]
        buy[0][0],sell[0][0] =-prices[0],0
        for i in range(1,k+1):
            buy[0][i]=sell[0][i]=float("-inf")
        for i in range(1,n):
            buy[i][0]=max(buy[i-1][0],sell[i-1][0]-prices[i])
            for j in range(1,k+1):
                buy[i][j]=max(buy[i-1][j],sell[i-1][j]-prices[i])
                sell[i][j]=max(sell[i-1][j],buy[i-1][j-1]+prices[i])
        return max(sell[n-1])
    def maxProfit1(self, k: int, prices: List[int]) -> int:
        if not k or len(prices)<2:return 0
        n=len(prices)
        k=min(k,n//2)
        buy,sell=[0]*(k+1),[0]*(k+1)
        buy[0],sell[0] =-prices[0],0
        for i in range(1,k+1):
            buy[i]=sell[i]=float("-inf")
        for i in range(1,n):
            buy[0]=max(buy[0],sell[0]-prices[i])
            for j in range(1,k+1):
                buy[j]=max(buy[j],sell[j]-prices[i])
                sell[j]=max(sell[j],buy[j-1]+prices[i])
        return max(sell)
    def maxProfit2(self, k: int, prices: List[int]) -> int:
        if not k or len(prices)<2:return 0
        n=len(prices)
        if k>=n//2:
            profit = 0
            for i in range(1,n):
                if prices[i]>prices[i-1]:profit+=prices[i]-prices[i-1]
            return profit
        t=[[0]*(n) for i in range(k+1)]
        for i in range(1,k+1):
            tmpMax=-prices[0]
            for j in range(1,n):
                t[i][j]=max(t[i][j-1],tmpMax+prices[j])
                tmpMax=max(tmpMax,t[i-1][j-1]-prices[j])
        return t[k][n-1]

    def maxProfit3(self, k: int, prices: List[int]) -> int:
        if not k or len(prices)<2:return 0
        n=len(prices)
        if k>=n//2: # k is big enougth to cover all ramps.
            return sum(i-j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        globalMax = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            # The max profit with i transations and selling stock on day j.
            localMax = [0] * n
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                localMax[j] = max(
                    # We have made max profit with (i - 1) transations in
                    # (j - 1) days.
                    # For the last transation, we buy stock on day (j - 1)
                    # and sell it on day j.
                    globalMax[i - 1][j - 1] + profit,
                    # We have made max profit with (i - 1) transations in
                    # (j - 1) days.
                    # For the last transation, we buy stock on day j and
                    # sell it on the same day, so we have 0 profit, apparently
                    # we do not have to add it.
                    globalMax[i - 1][j - 1],  # + 0,
                    # We have made profit in (j - 1) days.
                    # We want to cancel the day (j - 1) sale and sell it on
                    # day j.
                    localMax[j - 1] + profit)
                globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
        return globalMax[k][-1]
    def maxProfit4(self, k: int, prices: List[int]) -> int:
        if not k or len(prices)<2:return 0
        n=len(prices)
        if k>=n//2:
            maxProf = 0
            buy = prices[0]
            for i in range(1, n):
                maxProf +=max(0, prices[i]-prices[i-1])
            return maxProf
        dp =[[0]*n for _ in range(k+1)]
        for i in range(1, k+1):
            buy = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j], prices[j]+buy, dp[i][j-1])
                buy = max(buy, -prices[j]+dp[i-1][j-1])
        return dp[-1][-1]
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        * dp[i, j] represents the max profit up until prices[j] using at most i transactions. 
        * dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
        *          = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
        * dp[0, j] = 0; 0 transactions makes 0 profit
        * dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
        '''
        if not k or len(prices)<2:return 0
        n=len(prices)
        if k>=n//2:
            maxPro=0
            for i in range(1,n):
                if prices[i]>prices[i-1]:
                    maxPro += prices[i] - prices[i-1]
            return maxPro
        dp= [[0]*n for i in range(k+1)]
        for i in range(1,k+1):
            localMax=dp[i-1][0]-prices[0]
            for j in range(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j]+localMax)
                localMax=max(localMax,dp[i-1][j]-prices[j])
        return dp[k][n-1]
