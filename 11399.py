# 5
# 3 1 4 3 2

import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().split()))
b.sort()

# 1 2 3 3 4

answer = 0
for i in range(a):
    answer += sum(b[0:i+1])

print(answer)
