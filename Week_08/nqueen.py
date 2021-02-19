class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.count=0
        self.ans=[]
        queens=[0]*n
        self.dfs(n,0,0,0,0,queens)
        return [[ "".join(['Q' if i==s else '.' for i in range(n)]) for s in r] for r in self.ans]
    def dfs(self,n,row,cols,pies,nas,q):
        if row>=n:
            self.count+=1
            self.ans.append(q[:])
            return 
        bits = (~(cols|pies|nas))&((1<<n)-1)
        while bits:
            p=bits&-bits #取到最低位的1
            bits = bits&(bits-1) #去掉最低位的1
            column = bin(p-1).count("1")
            q[row]=column
            self.dfs(n,row+1,cols|p,(pies|p)<<1,(nas|p)>>1,q)
