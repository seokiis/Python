import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = int(input())
    dp = [0]*101
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    if (a >= 4):
        for j in range(4, a+1):
            dp[j] = dp[j-2]+dp[j-3]
    print(dp[a])
