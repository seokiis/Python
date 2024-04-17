import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []


def dfs(s):
    if len(answer) == M:
        print(*answer)
        return
    for s in range(s, N):
        answer.append(arr[s])
        dfs(s)
        answer.pop()


dfs(0)
