# 3
# 4
# 7
# 10

import sys
input = sys.stdin.readline

a = int(input())
for i in range(a):
    number = int(input())
    dp = [0]*(number+1)
    for i in range(1, number+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    print(dp[-1])
