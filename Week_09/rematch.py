class Solution:
    def isMatch0(self, s: str, p: str) -> bool:
        def dfs(string,pattern):
            if not pattern:return not string
            first_match = len(string)>0 and (string[0]==pattern[0] or pattern[0] == ".")
            if len(pattern)>1 and pattern[1]=="*":
                return dfs(string,pattern[2:]) or (first_match and dfs(string[1:],pattern))
            else:
                return first_match and dfs(string[1:],pattern[1:])
        return dfs(s,p)
    def isMatch0(self, s: str, p: str) -> bool:
        memo={}
        lenp,lens=len(p),len(s)
        def dfs(i,j):
            if (i,j) in memo:return memo[(i,j)]
            if j== lenp:return i==lens
            first_match = i<lens and (s[i]==p[j] or p[j] == ".")
            if lenp-j>1 and p[j+1]=="*":
                return dfs(i,j+2) or (first_match and dfs(i+1,j))
            else:
                return first_match and dfs(i+1,j+1)
        return dfs(0,0)
    def isMatch(self, s: str, p: str) -> bool:
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        table[0][0] = True
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    table[i][j] = table[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    table[i][j] = table[i - 2][j] or table[i - 1][j]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]
        return table[-1][-1]
    def isMatch0(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[-1][-1] = True
        for i in range(1,len(p)):
            dp[i][-1]=dp[i-2][-1] and p[i]=="*"
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i]=="*":
                    dp[i][j]=dp[i-2][j] or dp[i-1][j]
                    if p[i-1]==s[j] or p[i-1]==".":
                        dp[i][j] |= dp[i][j-1]
                else:
                    dp[i][j]=dp[i-1][j-1] and (p[i]==s[j] or p[i]==".")
        return dp[len(p)-1][len(s)-1]
    def isMatch0(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        dp=[[False]*(m+1) for i in range(n+1)]
        dp[-1][-1]=True
        for i in range(1,n):
            dp[i][-1]=dp[i-2][-1] and p[i]=="*"
        for i in range(n):
            for j in range(m):
                if p[i]=="*":
                    if dp[i-2][j] or dp[i-1][j]:
                        dp[i][j]=True
                    else:
                        if p[i-1]==s[j] or p[i-1]==".":
                            dp[i][j]=dp[i][j-1]
                else:
                    dp[i][j]=dp[i-1][j-1] and (p[i]==s[j] or p[i]==".")
        return dp[n-1][m-1]
    def isMatch0(self, s: str, p: str) -> bool:
        s, p = ' '+ s, ' '+ p
        lenS, lenP = len(s), len(p)
        dp = [[False]*(lenP) for i in range(lenS)]
        dp[0][0] = True
        for j in range(1, lenP):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-1] in {s[i], '.'})
        return dp[-1][-1]
    def isMatch(self, s: str, p: str) -> bool:
        if not p:return not s
        m,n = len(s), len(p)
        dp=[[False]*(n+1) for i in range(m+1)]
        dp[0][0]=True
        for j in range(1,n,2):
            dp[0][j+1]=p[j]=="*" and dp[0][j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                curS=s[i-1]
                curP=p[j-1]
                if curS==curP or curP==".":
                    dp[i][j]=dp[i-1][j-1]
                elif curP=="*":
                    b1=dp[i][j-2]
                    starBase=p[j-2]
                    b2=dp[i-1][j] and (starBase=='.' or starBase==curS)
                    dp[i][j]=b1 or b2
        return dp[m][n]
