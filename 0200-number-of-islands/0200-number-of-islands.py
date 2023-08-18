class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        island=0
        visited=set()
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            if(
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c]=="0"
                or (r,c) in visited
            ):
                return
            visited.add((r,c))
            dfs(r+1,c) 
            dfs(r-1,c) 
            dfs(r,c+1) 
            dfs(r,c-1) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    island+=1
                    dfs(r,c)
        return island