# 4 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 2 2 3 4
# 3 4 3 4
# 1 1 4 4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())


graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

dp[0][0] = graph[0][0]

# dp
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + graph[i - 1][j - 1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(answer)
