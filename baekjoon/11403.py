import sys
from collections import deque


# BFS
# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]


# def bfs(start):
#     queue = deque([start])
#     check = [0 for _ in range(n)]
#     while queue:
#         q = queue.popleft()
#         for node in range(n):
#             if graph[q][node] == 1 and check[node] == 0:
#                 check[node] = 1
#                 visited[start][node] = 1
#                 queue.append(node)


# for i in range(n):
#     bfs(i)

# for i in range(n):
#     print(visited(*i))


# DFS

# DFS
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]


def dfs(x):
    # 여기에 check=[0 for _ in range(n)]을 넣으면 dfs가 돌 때 마다 check가 초기화 됨! 그래서 못 넣음.
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


visited = [0 for _ in range(n)]
for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
    visited = [0 for _ in range(n)]
