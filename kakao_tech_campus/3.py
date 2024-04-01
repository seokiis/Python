import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * (N) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# x,y,direction,direction_changed,turn_count
queue = deque([(0, 0, 0, 0, 0), (0, 0, 2, 0, 0)])
visited[0][0] = 1
ans = 0

while queue:
    x, y, d, dc, tc = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if i == 0:
            nd = 0
        elif i == 1:
            nd = 1
        elif i == 2:
            nd = 2
        else:
            nd = 3

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                # 방향이 바꼈으면, nd,tc update
                if d != nd:
                    ndc = 1
                    tc += 1
                else:
                    ndc = 0
                queue.append((nx, ny, nd, ndc, tc))
            if nx == N - 1 and ny == N - 1:
                if tc == M:
                    ans = 1


if ans == 1:
    print("YES")
else:
    print("NO")


# 2 2
# 0 0
# 0 1
# YES

# 2 3
# 0 0
# 0 1
# NO
