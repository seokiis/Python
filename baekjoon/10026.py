# 우선 적록색맹이 아닐 때 영역의 개수를 구한다.
# R을 G로 바꿔준다.
# 적록색맹일 때 영역의 개수를 구한다.


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
visited = [[0] * n for _ in range(n)]
graph = [list(input().rstrip()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        now_color = graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue

            next_color = graph[nx][ny]
            if now_color == next_color and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1


ans_1 = 0
ans_2 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            ans_1 += 1

for i in range(n):
    for j in range(n):
        visited[i][j] = 0
        if graph[i][j] == "G":
            graph[i][j] = "R"


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            ans_2 += 1

print(ans_1, ans_2)
