class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res,cols,pie,na=[],[],[],[]
        def dfs(row,cur_stat):
            if row>=n:
                res.append(cur_stat)
                return
            for col in range(n):
                if col in cols or row+col in pie or row-col in na:
                    continue
                if col not in cols:cols.append(col)  #是否唯一都通过
                if row+col not in pie:pie.append(row+col)
                if row-col not in na:na.append(row-col)
                dfs(row+1,cur_stat+[col])
                cols.remove(col)
                pie.remove(row+col)
                na.remove(row-col)

        dfs(0,[])
        return self.genArray(res,n)
    def genArray(self,res,n):
        return [["."*i+"Q"+"."*(n-i-1) for i in r] for r in res]

class Solution0:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens,pie,na):
            if len(queens)==n:
                res.append(queens)
                return
            row=len(queens)
            for col in range(n):
                if col not in queens and row+col not in pie and row-col not in na:
                    dfs(queens+[col],pie+[row+col],na+[row-col])
        res=[]
        dfs([],[],[])
        return [["."*i+"Q"+"."*(n-i-1) for i in r] for r in res]
