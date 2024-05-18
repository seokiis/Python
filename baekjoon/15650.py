import sys
from itertools import combinations


input = sys.stdin.readline

N, M = map(int, input().split())

arr = []


def dfs(s):
    # 탈출조건
    if len(arr) == M:
        print(*arr)
        return
    for i in range(s, N + 1):
        if i not in arr:
            arr.append(i)
            dfs(i)
            arr.pop()


dfs(1)


# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
