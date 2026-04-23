class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        tree = [[] for _ in range(n)]
        for edge in edges: 
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        visited = set()

        def isTree(node: int, parent: int) -> bool:

            visited.add(node)
            for child in tree[node]:
                if child in visited:
                    if child != parent: return False
                    else: continue
                if not isTree(child, node):
                    return False
            return True

        return isTree(0, -1) and len(visited) == n