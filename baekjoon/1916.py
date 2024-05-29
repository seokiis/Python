# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
heap = []
costs = [1e9] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
heapq.heappush(heap, (start, 0))

while heap:
    point, path_sum = heapq.heappop(heap)
    # 현재 경로가 costs보다 크다면 pass
    # 이 부분에서는 >=가 되면 안되는 이유가 같은 경우도 if코드를 무시하고 아래 코드로 내려줘야함!! => 더 좋은 경로가 있을 수 있음!
    if path_sum > costs[point]:
        continue

    for next_point, path_weight in graph[point]:
        next_sum = path_weight + path_sum
        # 다음 노드까지 합이 costs보다 크다면 pass
        # 똑같은 것도 걸러주면 좋음 => 메모리 초과
        if next_sum >= costs[next_point]:
            continue
        costs[next_point] = next_sum
        heapq.heappush(heap, (next_point, next_sum))

print(costs[end])
