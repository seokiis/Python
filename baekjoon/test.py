# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 7
m = int(input())

graph = [[] for _ in range(n + 1)]
# 0 1 2 3 4 5 6 7
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

ans = []
visited = [0] * (n + 1)


def bfs(s):
    q = deque([])
    q.append(s)
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append(next_node)
                ans.append(next_node)
                visited[next_node] = 1


bfs(1)

print(len(ans))
