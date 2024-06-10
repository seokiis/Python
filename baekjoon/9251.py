import sys

input = sys.stdin.readline

line1 = " " + input().rstrip()
line2 = " " + input().rstrip()

print(line1)
print(line2)

dp = [[0] * len(line1) for _ in range(len(line2))]
print(dp)
# DP
for i in range(1, len(line1)):
    for j in range(1, len(line2)):
        # 같으면
        if line1[i] == line2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        # 다르면,
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])


# import sys

# string_a = ' ' + sys.stdin.readline().rstrip()
# string_b = ' ' + sys.stdin.readline().rstrip()
# dp = [[0] * len(string_b) for _ in range(len(string_a))]

# for i in range(1, len(string_a)):
#     for j in range(1, len(string_b)):
#         if string_a[i] == string_b[j]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print(dp[-1][-1])
