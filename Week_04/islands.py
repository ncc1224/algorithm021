class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        if not m:return 0
        count,n=0,len(grid[0])
        moves=[[1,0],[-1,0],[0,-1],[0,1]]
        def dfs(i,j):
            if i<m and i>=0 and j>=0 and j<n and grid[i][j]=="1":
                grid[i][j]="0"
                for mv in moves:
                    dfs(i+mv[0],j+mv[1])
        for x in range(m):
            for y in range(n):
                if grid[x][y]=="1":
                    count+=1
                    dfs(x,y)
        return count
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        if not m:return 0
        count,n=0,len(grid[0])
        moves=[[1,0],[-1,0],[0,-1],[0,1]]
        def inarea(i,j):
            if i>=0 and j>=0 and i<m and j<n:return True
            else:return False
        for x in range(m):
            for y in range(n):
                if grid[x][y]=="1":
                    count+=1
                    level=[(x,y)]
                    while level:
                        p=level.pop(0)
                        if inarea(p[0],p[1]) and grid[p[0]][p[1]]=="1":
                            grid[p[0]][p[1]]="0"
                            for mv in moves:
                                level.append((p[0]+mv[0],p[1]+mv[1]))
        return count
