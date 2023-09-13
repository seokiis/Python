# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

import sys
input = sys.stdin.readline

a = list()
n, m = map(int, input().split())
for i in range(n):
    a.append(int(input()))

count = 0
for i in reversed(range(n)):
    count += m//a[i]
    m %= a[i]
print(count)
