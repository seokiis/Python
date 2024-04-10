# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# result = 0
# visited = [[0] * m for _ in range(n)]


# def dfs(i, j, count, total_sum):
#     global result

#     if count == 4:
#         result = max(result, total_sum)

#     else:
#         for k in range(4):
#             nx = i + dx[k]
#             ny = j + dy[k]
#             if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
#                 visited[nx][ny] = 1
#                 dfs(nx, ny, count + 1, total_sum + arr[nx][ny])
#                 visited[nx][ny] = 0


# def block(i, j, total_sum):
#     make = 0
#     global result

#     for k in range(4):
#         next_i = i + dx[k]
#         next_j = j + dy[k]
#         if 0 <= next_i < n and 0 <= next_j < m:
#             make += 1
#             total_sum += arr[next_i][next_j]
#     if make == 3:
#         result = max(result, total_sum)
#     if make == 4:
#         for p in range(4):
#             prev_i = i + dx[p]
#             prev_j = j + dy[p]
#             total_sum -= arr[prev_i][prev_j]
#             result = max(result, total_sum)
#             total_sum += arr[prev_i][prev_j]


# for i in range(n):
#     for j in range(m):
#         visited[i][j] = 1
#         dfs(i, j, 1, arr[i][j])
#         block(i, j, arr[i][j])
#         visited[i][j] = 0

# print(result)

import sys

input = sys.stdin.readline


def dfs(r, c, idx, total):
    global ans
    # 백트래킹을 통해 중복 탐색을 줄이고 효율적인 탐색을 위해 사용됩니다.
    # 만약 현재 탐색 중인 경로의 값이 이미 구한 최대값보다 작거나 같으면 해당 경로를 더 이상 탐색하지 않고 종료합니다.
    if ans >= total + (3 - idx) * max_val:
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if idx == 1:
                    visited[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visited[nr][nc] = 0
                visited[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visited[nr][nc] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0
max_val = max(map(max, arr))


for r in range(n):
    for c in range(m):
        visited[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visited[r][c] = 0

print(ans)
