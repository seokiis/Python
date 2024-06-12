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

# 다익스트라
# 1.시작 정점에서 가장 가까운 정점을 선택합니다.
# 2.해당 정점을 경유지로 하여 다른 정점으로의 경로를 고려하여 최단 거리를 갱신합니다.
# 3.방문하지 않은 노드들 중 최단 거리가 가장 짧은 노드를 선택합니다.
# 4.3번 과정을 반복하면서 모든 노드를 방문할 때까지 최단 경로를 갱신해 나갑니다.

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
    #  이미 방문한 노드이면 스킵(여기까지의 경로가 다른 경로에 의해 업데이트 된 경로보다 크다면 무시해야함)
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
