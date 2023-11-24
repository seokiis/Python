# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

import sys
input = sys.stdin.readline

number = int(input())


dp = [0]*(number+1)
for i in range(2, number+1):
    dp[i] = dp[i-1]+1
    # if로 해놔야 %3, %2 둘 다 체크함
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[number])
