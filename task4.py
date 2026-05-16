NAME: BRIAN KIPLANG'AT ROTICH
REG NO: CIT-227-078/2024
TASK 4: BFS AND DFS PATHFINDING
IMPLEMENTATION
Description: This document contains the complete executable Python script implementing Breadth-First
Search (BFS) and Depth-First Search (DFS) algorithms to find a path between a start node and a goal node
within a graph structure. The DFS implementation includes standard backtracking logic to prevent state
pollution and guarantee correct path discovery across complex topologies.
SOURCE CODE (TASK4.PY)
# NAME: BRIAN KIPLANG'AT ROTICH
# REG NO: CIT-227-078/2024
# task4.py - BFS and DFS from start to goal
# Uses a simple graph, prints the path found
from collections import deque
# The graph used for testing
graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}
# BFS using a queue
def bfs(graph, start, goal):
 queue = deque([[start]])
 visited = set([start])
while queue:
 path = queue.popleft()
 node = path[-1]
if node == goal:
return path
for neighbor in graph[node]:
if neighbor not in visited:
 visited.add(neighbor)
1 queue.append(path + [neighbor])
return None
# DFS using recursion
def dfs(graph, start, goal, visited=None, path=None):
if visited is None:
 visited = set()
if path is None:
 path = [start]
 visited.add(start)
if start == goal:
return path
for neighbor in graph[start]:
if neighbor not in visited:
 result = dfs(graph, neighbor, goal, visited, path + [neighbor])
if result:
return result
 visited.remove(start)
return None
# Testing both functions
if __name__ == "__main__":
 start = 'A'
 goal = 'F'
print("Graph:")
for node in graph:
print(f"{node}: {graph[node]}")
print(f"\nStarting BFS from {start} to {goal}")
 bfs_result = bfs(graph, start, goal)
print("BFS path:", bfs_result)
print(f"\nStarting DFS from {start} to {goal}")
 dfs_result = dfs(graph, start, goal)
print("DFS path:", dfs_result)
