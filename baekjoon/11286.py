import sys
import heapq

input = sys.stdin.readline


heap = []
n = int(input())


for _ in range(n):
    number = int(input())
    # 절댓값 가장 작은 수 추출, 여러개라면 가장 작은 값 출
    if number:
        heapq.heappush(heap, (abs(number), number))

    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
