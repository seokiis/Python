import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방향
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 현재 위치 y, x , 회전 횟수, 현재 방향
queue = deque()
queue.append((0, 0, 0, 0))
queue.append((0, 0, 0, 1))
# 현재 위치 방문 체크
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1

while queue:
    cury, curx, k, d = queue.popleft()
    if curx == N - 1 and cury == N - 1:
        if k == K:
            print("YES")
            sys.exit(0)
        else:
            continue
    # 현재 방향으로 1칸 이동하는 경우
    dir_y, dir_x = dir[d]
    newy, newx = cury + dir_y, curx + dir_x
    if (
        0 <= newx < N
        and 0 <= newy < N
        and visited[newy][newx] == 0
        and graph[newy][newx] == 0
    ):
        queue.append((newy, newx, k, d))
    # 왼쪽 또는 오른쪽으로 회전하는 경우
    if d - 1 < 0:
        leftd = 3
    else:
        leftd = d - 1
    dir_y, dir_x = dir[leftd]
    newy, newx = cury + dir_y, curx + dir_x
    if (
        0 <= newx < N
        and 0 <= newy < N
        and visited[newy][newx] == 0
        and graph[newy][newx] == 0
    ):
        queue.append((newy, newx, k + 1, leftd))

    if d + 1 > 3:
        rightd = 0
    else:
        rightd = d + 1
    dir_y, dir_x = dir[rightd]
    newy, newx = cury + dir_y, curx + dir_x
    if (
        0 <= newx < N
        and 0 <= newy < N
        and visited[newy][newx] == 0
        and graph[newy][newx] == 0
    ):
        queue.append((newy, newx, k + 1, rightd))
else:
    print("NO")
