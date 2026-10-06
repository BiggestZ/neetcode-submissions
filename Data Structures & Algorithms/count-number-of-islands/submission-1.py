class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate, find '1', perform BFS increment
        if not grid:
            return 0
        visited = set()
        num_islands = 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        #BFS Helper
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr in range(rows) and nc in range(cols) and
                    (nr, nc) not in visited and grid[nr][nc] =='1'):
                        q.append((nr,nc))
                        visited.add((nr,nc))
        #Iterate entire grid
        for r in range(rows):
            for c in range(cols):
                # Land check
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    num_islands += 1
        return num_islands

        