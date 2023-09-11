# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

a = set()
b = set()

for i in range(n):
    a.add(input().strip())

for i in range(m):
    b.add(input().strip())

result = sorted(a & b)
print(len(a & b))
for i in result:
    print(i)
