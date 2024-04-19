# # 8
# # 71 39 44
# # 32 83 55
# # 51 37 63
# # 89 29 100
# # 83 58 11
# # 65 13 15
# # 47 25 29
# # 60 66 19

# bfs는 시간 초과

# import sys
# from collections import deque


# input = sys.stdin.readline

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]


# q = deque([])
# q.append((arr[0][0], 0, 0))
# q.append((arr[0][1], 0, 1))
# q.append((arr[0][2], 0, 2))

# ans = []

# while q:
#     now_sum, count, idx = q.popleft()
#     if count == n - 1:
#         ans.append(now_sum)
#     if count < n - 1:
#         if idx == 0:
#             q.append((now_sum + arr[count + 1][1], count + 1, 1))
#             q.append((now_sum + arr[count + 1][2], count + 1, 2))
#         elif idx == 1:
#             q.append((now_sum + arr[count + 1][0], count + 1, 0))
#             q.append((now_sum + arr[count + 1][2], count + 1, 2))
#         elif idx == 2:
#             q.append((now_sum + arr[count + 1][0], count + 1, 0))
#             q.append((now_sum + arr[count + 1][1], count + 1, 1))


# print(min(ans))

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] = min(arr[i][0] + arr[i - 1][1], arr[i][0] + arr[i - 1][2])
    arr[i][1] = min(arr[i][1] + arr[i - 1][0], arr[i][1] + arr[i - 1][2])
    arr[i][2] = min(arr[i][2] + arr[i - 1][1], arr[i][2] + arr[i - 1][0])

print(min(arr[n - 1][0], arr[n - 1][1], arr[n - 1][2]))
