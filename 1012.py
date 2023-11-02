# 그래프의 각 칸을 차례대로 돌다가 1을 만나면 0으로 바꿔주고,
# BFS를 수행한다.
# 인접한 1은 0으로 바꼈기 때문에
# 1칸을 발견할 때마다 cnt를 증가시킨다.

# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5


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
            nx = x+dx[i]
            ny = y+dy[i]
            if (nx < 0 or nx >= m or ny >= n or ny < 0):
                continue

            if (graph[ny][nx] == 1):
                graph[ny][nx] = 0
                queue.append((nx, ny))
    return


number = int(input())
for i in range(number):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
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
