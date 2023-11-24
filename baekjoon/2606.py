# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

from collections import deque
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

# graph
graph = [[]for _ in range(a+1)]

# graph 채우기
for i in range(b):
    m, n = map(int, input().split())
    graph[m] += [n]
    graph[n] += [m]

# visiited
visited = [0]*(a+1)

# BFS
queue = deque([1])
visited[1] = 1
while queue:
    nx = queue.popleft()
    for node in graph[nx]:
        # 방문하지 않은 노드라면 방문 표시하고 append
        if visited[node] == 0:
            queue.append(node)
            visited[node] = 1
print(sum(visited)-1)
