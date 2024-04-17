# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
import sys

sys.setrecursionlimit(10**6)
n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(s):
    for node in graph[s]:
        if parent[node] == 0:
            parent[node] = s
            dfs(node)


dfs(1)
for i in range(2, n + 1):
    print(parent[i])
