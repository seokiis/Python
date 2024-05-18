# # 4 2
# # 1 7 8 9
# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()


# answer = []


# def dfs(s):
#     if len(answer) == M:
#         print(*answer)
#         return
#     for i in range(N):
#         if arr[i] not in answer:
#             answer.append(arr[i])
#             dfs(s + 1)
#             answer.pop()


# dfs(0)


import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

temp = []
# 1 7 8 9


def dfs(depth):
    if depth == M:
        print(*temp)
        return
    for i in range(N):
        if arr[i] not in temp:
            temp.append(arr[i])

            dfs(depth + 1)
            temp.pop()


dfs(0)
