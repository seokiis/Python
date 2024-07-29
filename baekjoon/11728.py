import sys

input = sys.stdin.readline
import heapq
from heapq import heapify

N, M = map(int, input().split())

L = list(map(int, input().split()))
heapify(L)


L_2 = list(map(int, input().split()))

for i in range(M):
    heapq.heappush(L, L_2[i])


for i in range(N + M):
    print(heapq.heappop(L), end=" ")
