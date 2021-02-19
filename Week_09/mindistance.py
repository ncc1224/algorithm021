class Solution:
    def minDistance0(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if not m or not n:return max(m,n)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            dp[i][-1]=dp[i-1][-1]+1
        for j in range(n):
            dp[-1][j]=dp[-1][j-1]+1
        for i in range(m):
            for j in range(n):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[m-1][n-1]
    def minDistance0(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if not m or not n:return max(m,n)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            dp[i][0]=dp[i-1][0]+1
        for j in range(1,n+1):
            dp[0][j]=dp[0][j-1]+1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[m][n]
    def minDistance0(self, word1: str, word2: str) -> int: #长了会超时 加缓存
        m,n=len(word1),len(word2)
        if not m or not n:return max(m,n)
        def dfs(i,j,memo):
            if i==m:return n-j
            if j==n:return m-i
            if (i,j) in memo:
                return memo[(i,j)]
            else:
                if word1[i]==word2[j]:
                    ret = dfs(i+1,j+1,memo)
                else:
                    ret=1+min(dfs(i+1,j,memo),dfs(i,j+1,memo),dfs(i+1,j+1,memo))
                memo[(i,j)]=ret
                return ret
        return dfs(0,0,{})
    def minDistance0(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if not m or not n:return max(m,n)
        def dfs(i,j,memo):
            if i<0:return j
            if j<0:return i
            if (i,j) not in memo:
                if word1[i]==word2[j]:
                    ret = dfs(i-1,j-1,memo)
                else:
                    ret=1+min(dfs(i-1,j,memo),dfs(i,j-1,memo),dfs(i-1,j-1,memo))
                memo[(i,j)]=ret
            print(memo)
            return memo[(i,j)]
        return dfs(m-1,n-1,{})
    def minDistance0(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if not m or not n:return max(m,n)
        pre,curr=[0]*(n+1),[0]*(n+1)
        for i in range(1,n+1):
            pre[i]=i
        for i in range(1,m+1):
            curr[0]=i
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    curr[j]=pre[j-1]
                else:
                    curr[j]=min(curr[j-1],pre[j-1],pre[j])+1
            pre[:]=curr[:]
        return curr[-1]
    def minDistance0(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if not m or not n:return max(m,n)
        curr=[0]*(n+1)
        for i in range(1,n+1):
            curr[i]=i
        for i in range(1,m+1):
            pre=curr[0]
            curr[0]=i
            for j in range(1,n+1):
                temp=curr[j]
                if word1[i-1]==word2[j-1]:
                    curr[j]=pre
                else:
                    curr[j]=min(curr[j-1],pre,curr[j])+1
                pre=temp
        return curr[-1]
    def minDistance0(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [list(range(n+1))]+[[r+1]+[0]*n for r in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j] if word1[i]==word2[j] else min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
        return dp[m][n]

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        curr = list(range(n+1))
        for i in range(m):
            prev, curr = curr, [i+1] + [0] * n
            for j in range(n):
                curr[j+1] = prev[j] if word1[i] == word2[j] else min(curr[j], prev[j], prev[j+1]) + 1
        return curr[n]
