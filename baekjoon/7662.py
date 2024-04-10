# D 1 최댓값 삭제
# D -1 최솟값 삭제
# 2개가 있는 경우 1개만 삭제
# 비어있는데 D라면 무시
# 최종 최댓값, 최솟값 표시

# heapq를 쓸 것 같다.
# 최소힙, 최대힙

import heapq
import sys

input = sys.stdin.readline

total_num = int(input())
for _ in range(total_num):
    max_heap = []
    min_heap = []
    visited = [False] * 1_000_001
    k = int(input())
    for i in range(k):
        command, num = input().strip().split()
        if command == "I":
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
            visited[i] = True
        else:
            if num == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
