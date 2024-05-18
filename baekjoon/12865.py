# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]
bag = []


for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j >= bag[i - 1][0]:
            dp[i][j] = max(dp[i - 1][j], bag[i - 1][1] + dp[i - 1][j - bag[i - 1][0]])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
