class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        component_count = 0
        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def scan(node: int):
            if node in visited: return
            visited.add(node)
            for neigh in graph[node]:
                scan(neigh)

        for node in range(n):
            if node not in visited:
                component_count += 1
                scan(node)

        return component_count
