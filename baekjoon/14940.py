import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny >= m or ny < 0:
                continue
            #  0 ,1
            if graph[nx][ny] == 0:
                visited[nx][ny] = 0
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()

# for i in visited:
#     print(*i)
