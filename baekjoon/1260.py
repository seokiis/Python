# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

from collections import deque

# dfs


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# bfs


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m, v = map(int, input().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False]*(n+1)
dfs(v)
print()

# bfs
visited = [False]*(n+1)
bfs(v)
