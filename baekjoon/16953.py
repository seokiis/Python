import sys

input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())


def bfs(s):
    q = deque([(s, 1)])
    while q:
        now, count = q.popleft()

        if now > b:
            continue

        if now == b:
            print(count)
            break

        q.append((now * 2, count + 1))
        q.append((int(str(now) + "1"), count + 1))

    else:
        print(-1)


bfs(a)

print()
