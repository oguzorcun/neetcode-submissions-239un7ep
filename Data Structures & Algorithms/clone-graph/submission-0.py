"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if not node: return
            if node in visited: return visited[node]

            new_node = Node(node.val, [])
            visited[node] = new_node

            for nb in node.neighbors:
                new_node.neighbors.append(dfs(nb))

            return new_node

        return dfs(node)        