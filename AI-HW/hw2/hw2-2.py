from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                result.append(node)
                visited.add(node)
                queue.extend([neighbor for neighbor in self.graph[node] if neighbor not in visited])

        return result
    
    def dfs(self, start):
        visited = set()
        result = []

        def dfs_util(node):
            visited.add(node)
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)
        return result

# Example 1: Creating a graph and performing BFS
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS traversal (starting from vertex 2):")
result = g.bfs(2)
print(result)
print("DFS traversal (starting from vertex 2):")
result = g.dfs(2)
print(result)

# Example 2: Creating another graph and performing BFS
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('A', 'C')
g2.add_edge('B', 'D')
g2.add_edge('B', 'E')
g2.add_edge('C', 'F')

print("\nBFS traversal (starting from vertex 'A'):")
result2 = g2.bfs('A')
print(result2)
print("\nDFS traversal (starting from vertex 'A'):")
result2 = g2.dfs('A')
print(result2)
