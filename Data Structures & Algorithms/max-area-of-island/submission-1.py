class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #For each island we run BFS, and increment on each, then compare to max., return max at end
        # 0 if not grid
        if not grid:
            return 0

        visited = set()
        rows,cols = len(grid), len(grid[0])
        max_area = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]   
        counter = 0 

        #Iterate thru grid
        for r in range(rows):
            for c in range(cols):
                # If unvisited land:
                if grid[r][c] == 1 and (r,c) not in visited:
                    counter = 1
                    q = deque()
                    # Add to queue and visited set
                    q.append((r,c))
                    visited.add((r,c))
                    while q:
                        row, col = q.pop() #Pops like a stack, newest first
                        for dr, dc in directions:
                            nr, nc = row+dr, col+dc
                            # Check in-bounds + meets condition
                            if (nr in range(rows) and nc in range(cols) and 
                            grid[nr][nc] == 1 and (nr,nc) not in visited):
                                q.append((nr,nc))
                                visited.add((nr,nc))
                                counter +=1
                            # Once traverse queue, compare to previous max    
                    max_area = max(max_area, counter)
                                
        return max_area
