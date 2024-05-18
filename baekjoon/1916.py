# import sys
# from collections import deque

# # 메모리 초과

# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     graph[a].append((b, cost))

# start, end = map(int, input().split())


# # 작성한 코드에는 도시까지의 비용이 같은 경우에 큐에 여러번 들어가는 문제가 있었다.
# # ex) 도시 4 까지 가는 방법이 여러개이고 그 비용이 같은 경우 1→ 4(4), 1→2→4 (4)


# def bfs(start):
#     min_cost = 1e7
#     q = deque()
#     q.append([start, 0])
#     while q:
#         cur_v, cur_cost = q.popleft()
#         if cur_v == end and cur_cost < min_cost:
#             min_cost = cur_cost
#         for v, c in graph[cur_v]:
#             if (v, cur_cost + c) in q:
#                 continue
#             q.append((v, cur_cost + c))

#     return min_cost


# print(bfs(start))

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())
costs = [1e9 for _ in range(n + 1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])

while heap:
    cur_cost, cur_v = heapq.heappop(heap)
    # 현재 노드(a)까지 오는 데 누적되었던 비용이(cur_cost) 다른 길을 통해서 구한 최소 비용(costs[cur_v])보다 크다면 continue
    if costs[cur_v] < cur_cost:
        continue
    # 현재 노드에서 다음 노드로 이동하는 데 비용을 더한 값이 그동안 계산된 costs[nest_v]보다 크다면 continue
    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_v]:
            continue

        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])

print(costs[end])
