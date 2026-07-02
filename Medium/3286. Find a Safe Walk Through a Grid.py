from typing import List
import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        health -= grid[0][0]
        if health <= 0:
            return False

        pq = [(-health, 0, 0)]  # (remaining_health, row, col)
        best = [[-1] * n for _ in range(m)]
        best[0][0] = health

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            curr_health, r, c = heapq.heappop(pq)
            curr_health = -curr_health

            if r == m - 1 and c == n - 1:
                return True

            if curr_health < best[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_health = curr_health - grid[nr][nc]

                    if new_health > 0 and new_health > best[nr][nc]:
                        best[nr][nc] = new_health
                        heapq.heappush(pq, (-new_health, nr, nc))

        return False
