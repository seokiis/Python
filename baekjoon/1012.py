from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny >= n or ny < 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx, ny))
    return


number = int(input())
for i in range(number):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0

    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                bfs(graph, x, y)
                cnt += 1
    print(cnt)
