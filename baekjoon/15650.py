import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []


def dfs(s):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(s, N + 1):
        arr.append(i)
        dfs(i)
        arr.pop()


dfs(1)
