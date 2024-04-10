# 최소한의 명령어 사용
# BFS로 풀어야함

import sys
from collections import deque

input = sys.stdin.readline


number = int(input())
for i in range(number):
    A, B = map(int, input().strip().split())
    visited = [0] * 10001

    q = deque([(A, "")])
    visited[A] = True

    while q:
        num, command = q.popleft()

        if num == B:
            print(command)
            break

        D = num * 2 % 10000
        if not visited[D]:
            q.append((D, command + "D"))
            visited[D] = True

        S = (num - 1) % 10000
        if not visited[S]:
            q.append((S, command + "S"))
            visited[S] = True

        L = num // 1000 + (num % 1000) * 10
        if not visited[L]:
            q.append((L, command + "L"))
            visited[L] = True

        R = num // 10 + (num % 10) * 1000
        if not visited[R]:
            q.append((R, command + "R"))
            visited[R] = True
