class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        component_count = 0
        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def scan(node: int):
            for neigh in graph[node]: 
                if neigh not in visited:
                    visited.add(neigh) 
                    scan(neigh)

        for node in range(n):
            if node not in visited:
                component_count += 1
                visited.add(node)
                scan(node)

        return component_count
