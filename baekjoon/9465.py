import sys

input = sys.stdin.readline


n = int(input())
for i in range(n):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * k for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if k == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if k == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for j in range(2, k):
        dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + arr[0][j]
        dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + arr[1][j]

    print(max(dp[0][-1], dp[1][-1]))
