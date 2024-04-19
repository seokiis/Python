# 4 2
# 9 7 9 1
# 1 7 9 9

# 1 1
# 1 7
# 1 9
# 7 7
# 7 9
# 9 9

# dfs에서 pop된 걸 다시 안 넣는다!!

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * n

arr.sort()
ans = []


def dfs(s):
    if len(ans) == m:
        print(*ans)
        return
    # 새로운 dfs 들어갈 때 마다 remember_me 초기화
    remember_me = 0
    # 1 7 9 9

    for i in range(s, n):
        if remember_me != arr[i]:
            remember_me = arr[i]
            ans.append(arr[i])
            dfs(i)
            ans.pop()


dfs(0)
