class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:return 0
        m,n,t1,t2=len(text1),len(text2),list(text1),list(text2)
        dp=[[0]*n for i in range(m)]
        dp[0][0]=1 if t1[0]==t2[0] else 0
        for j in range(1,n):
            dp[0][j]=dp[0][j-1] if dp[0][j-1] else (1 if t1[0]==t2[j] else 0)
        for i in range(m):
            tmp=1 if t1[i]==t2[0] else 0
            dp[i][0]=dp[i-1][0] if dp[i-1][0] else (1 if t1[i]==t2[0] else 0)
        for i in range(1,m):
            for j in range(1,n):
                if t1[i]==t2[j]:
                    dp[i][j] =dp[i-1][j-1] + 1
                else:
                    dp[i][j]=dp[i][j-1] if dp[i][j-1]>dp[i-1][j] else dp[i-1][j]
        return dp[m-1][n-1]
                
class Solution0:
    def longestCommonSubsequence0(self, text1: str, text2: str) -> int:
        if not text1 or not text2:return 0
        m,n=len(text1),len(text2)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] =dp[i-1][j-1] + 1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[m][n]
    def longestCommonSubsequence0(self, text1: str, text2: str) -> int:
        if not text1 or not text2:return 0
        m,n=len(text1),len(text2)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    dp[i][j] =dp[i-1][j-1] + 1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[m-1][n-1]
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        if not text1 or not text2:return 0
        m,n,k=len(text1),len(text2),1
        if m<n:return self.longestCommonSubsequence(text2,text1)
        dp=[[0]*(n+1) for i in range(2)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[k][j]=dp[k^1][j-1]+1 if c==d else max(dp[k^1][j],dp[k][j-1])
            k^=1
        return dp[k^1][n-1]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:return 0
        m,n=len(text1),len(text2)
        if m<n:return self.longestCommonSubsequence(text2,text1)
        dp=[0]*(n+1)
        for i, c in enumerate(text1):
            prevRow, prevRowPrevCol = 0, 0
            for j, d in enumerate(text2):
                prevRow, prevRowPrevCol = dp[j], prevRow
                dp[j]=prevRowPrevCol+1 if c==d else max(dp[j-1],prevRow)
        return dp[n-1]
import functools
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.lru_cache(None)
        def helper(i,j):
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return helper(i-1,j-1)+1
            return max(helper(i-1,j),helper(i,j-1))
        return helper(len(text1)-1,len(text2)-1)
