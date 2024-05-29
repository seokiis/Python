import sys

input = sys.stdin.readline


# 슬라이딩 윈도우란?

# dp에서 메모이제이션을 할 때, 사용하지 않는 값을 배열에 저장하지 않고 배열을 새롭게 계속해서 갱신시켜주는 것이다.


# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# max_dp = [[0] * 3 for _ in range(n)]
# min_dp = [[0] * 3 for _ in range(n)]

# # 기본 dp
# for i in range(3):
#     max_dp[0][i] = graph[0][i]
#     min_dp[0][i] = graph[0][i]

# for i in range(1, n):
#     for j in range(3):
#         if j == 0:
#             max_dp[i][j] = graph[i][j] + max(max_dp[i - 1][0], max_dp[i - 1][1])
#             min_dp[i][j] = graph[i][j] + min(min_dp[i - 1][0], min_dp[i - 1][1])
#         elif j == 1:
#             max_dp[i][j] = graph[i][j] + max(
#                 max_dp[i - 1][0], max_dp[i - 1][1], max_dp[i - 1][2]
#             )
#             min_dp[i][j] = graph[i][j] + min(
#                 min_dp[i - 1][0], min_dp[i - 1][1], min_dp[i - 1][2]
#             )
#         else:
#             max_dp[i][j] = graph[i][j] + max(max_dp[i - 1][1], max_dp[i - 1][2])
#             min_dp[i][j] = graph[i][j] + min(min_dp[i - 1][1], min_dp[i - 1][2])

# print(max(max_dp[n - 1]), min(min_dp[n - 1]))

n = int(input())


min_dp = [0] * 3

max_dp = list(map(int, input().split()))
for i in range(3):
    min_dp[i] = max_dp[i]

max_temp = [0] * 3
min_temp = [0] * 3


for i in range(1, n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_temp[0] = a + max(max_dp[0], max_dp[1])
            min_temp[0] = a + min(min_dp[0], min_dp[1])
        elif j == 1:
            max_temp[1] = b + max(max_dp[0], max_dp[1], max_dp[2])
            min_temp[1] = b + min(min_dp[0], min_dp[1], min_dp[2])
        else:
            max_temp[2] = c + max(max_dp[1], max_dp[2])
            min_temp[2] = c + min(min_dp[1], min_dp[2])

    for k in range(3):
        max_dp[k] = max_temp[k]
        min_dp[k] = min_temp[k]


print(max(max_dp), min(min_dp))
