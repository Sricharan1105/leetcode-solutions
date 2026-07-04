from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        visited = set()
        stack = [1]
        answer = float('inf')

        while stack:
            city = stack.pop()

            if city in visited:
                continue

            visited.add(city)

            for neighbour, distance in graph[city]:
                answer = min(answer, distance)

                if neighbour not in visited:
                    stack.append(neighbour)

        return answer
