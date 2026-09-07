import heapq

class Solution:
    def swimInWater(self, grid):

        n = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visited = set()

        while heap:

            time, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            time = max(time, grid[r][c])

            if r == n - 1 and c == n - 1:
                return time

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    heapq.heappush(
                        heap,
                        (max(time, grid[nr][nc]), nr, nc)
                    )