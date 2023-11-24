# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
array = list(map(int, input().split()))

prefix_sum = [0]

temp = 0
for number in array:
    temp += number
    prefix_sum.append(temp)

for j in range(n):
    start, end = map(int, input().split())
    print(prefix_sum[end]-prefix_sum[start-1])
