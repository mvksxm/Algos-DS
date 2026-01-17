from collections import deque

class Solution:
    def maxAreaOfIsland(grid: list) -> int:

        if not grid or not grid[0]:
            return 0

        max_area= 0
        visited_set = set()
        len_rows = len(grid)
        len_cols = len(grid[0])

        def bfs(row, col):
            island_area = 0
            queue = deque()
            queue.append((row, col))
            visited_set.add((row, col))
            island_area += 1

            while queue:
                first_elem = queue.popleft()
                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

                for dr in directions:
                    new_row = first_elem[0] + dr[0]
                    new_col = first_elem[1] + dr[1]

                    if new_row in range(len_rows) and new_col in range(len_cols) \
                            and grid[new_row][new_col] == 1 \
                            and (new_row, new_col) not in visited_set:
                        island_area += 1
                        queue.append((new_row, new_col))
                        visited_set.add((new_row, new_col))

            return island_area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited_set:
                    area = bfs(r, c)
                    max_area = max(area, max_area)

        return max_area

grid=[[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]
print(Solution.maxAreaOfIsland(grid))