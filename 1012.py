# 그래프의 각 칸을 차례대로 돌다가 1을 만나면 0으로 바꿔주고,
# BFS를 수행한다.
# 인접한 1은 0으로 바꼈기 때문에
# 1칸을 발견할 때마다 cnt를 증가시킨다.

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    # deque는 배열이다.
    queue = deque()
    # queue=[(a,b),(a,b),,,]
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))
    return


t = int(input())

for i in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]  # n*m

    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
