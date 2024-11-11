class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        m=len(grid) 
        n=len(grid[0])
        visited=[[False] * n for _ in range(m)]
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>= n or grid[r][c]=='W' or visited[r][c]:
                 return
            visited[r][c]=True
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        count=0

        for r in range(m):
            for c in range(n):
                if grid[r][c]=='L' and not visited[r][c]:
                    dfs(r,c)
                    count+=1
        return count

