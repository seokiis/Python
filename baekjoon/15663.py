# 4 2
# 9 7 9 1
# 1 7 9 9

# 1 7
# 1 9
# 7 1
# 7 9
# 9 1
# 9 7
# 9 9

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * (N + 1)
ans = []


def dfs(s):
    if len(ans) == M:
        print(*ans)
        return
    # 새로운 친구 먹을 때(새로 dfs시작할 때)는 초기화 해줘야 같은 녀석도 먹는다.
    remember_me = 0
    for i in range(N):
        # 방문하지 않았고,
        if not visited[i] and remember_me != arr[i]:
            # pop 해서 나왔을 때, remember_me를 체크하게 된다. 방금 pop되기 . 전녀석을 기억하고 check.
            remember_me = arr[i]
            visited[i] = 1
            ans.append(arr[i])
            dfs(s + 1)
            visited[i] = 0
            ans.pop()


dfs(0)
