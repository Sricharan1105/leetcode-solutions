class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    x, y = dfs(nei)
                    nodes += x
                    edge_count += y

            return nodes, edge_count

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)

                if edge_count == nodes * (nodes - 1):
                    ans += 1

        return ans
