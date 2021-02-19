class Solution:
    def solveSudoku0(self, board: List[List[str]]) -> None:
        rows=[set(range(1,10)) for i in range(9)]
        cols=[set(range(1,10)) for i in range(9)]
        block=[set(range(1,10)) for i in range(9)]
        empty=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    empty.append((i,j))
                else:
                    val=int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    block[((i//3)*3+j//3)].remove(val)
        empcnt=len(empty)
        def dfs(level=0):
            if level==empcnt:return True
            i,j=empty[level]
            b=(i // 3)*3 + j // 3
            for val in rows[i]&cols[j]&block[b]:
                rows[i].remove(val)
                cols[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if dfs(level+1):return True
                rows[i].add(val)
                cols[j].add(val)
                block[b].add(val)
            return False
        dfs(0)

    def solveSudoku0(self, board: List[List[str]]) -> None:
        def validate(i,j,flag):
            for k in range(9):
                if board[i][k]!=".":
                    flag[int(board[i][k])]=False
                if board[k][j]!=".":
                    flag[int(board[k][j])]=False
                r,c=i//3*3+k//3,j//3*3+k%3
                if board[r][c]!=".":
                    flag[int(board[r][c])]=False
        def dfs(d):
            if d==81:return True
            i,j=d//9,d%9
            if board[i][j]!=".":return dfs(d+1)
            flag=[True for i in range(10)]
            validate(i,j,flag)
            for k in range(1,10):
                if flag[k]:
                    board[i][j]=str(k)
                    if dfs(d+1):
                        return True
            board[i][j]="."
            return False
        dfs(0)
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(row,col,val):
            for i in range(9):
                if board[row][i]==val:return False
                if board[i][col]==val:return False
            x,y=row//3*3,col//3*3
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if board[i][j]==val:return False
            return True
        def dfs():
            for i in range(9):
                for j in range(9):
                    if board[i][j]!=".":continue
                    for k in range(1,10):
                        if not isValid(i,j,str(k)):continue
                        board[i][j]=str(k)
                        if dfs():return True
                        board[i][j]="."
                    return False
            return True
        dfs()
