#다익스트라
#그래프에서 하나의 노드에서 각각의 노드까지 최단거리를 구하는 ~

#이웃이 여러개니까 set
from collections import defaultdict
from heapq import heappop,heappush

def solution(n,paths,gates,summits):
  graph=defaultdict(set)
  for i,j,w in paths:
    graph[i].add((j,w))
    graph[j].add((i,w))

  intensities=[float('inf')]*(n+1)
  heap=[]
  for gate in gates:
    intensities[gate]=0
    heappush(heap,(0,gate))

  while heap:
    i,n=heappop(heap)
    # 현재까지 발견된 해당 노드 n까지의 최단 거리(intensities[n])보다 현재 경로의 거리 i가 더 짧은 경우에는 더 이상 해당 노드로 가는 경로를 탐색할 필요가 없기 때문에 무시하는 조건입니다. 
    if intensities[n]<i or n in summits:
      continue
    for j, ji in graph[n]:
      ni=max(i,ji)
      if intensities[j]>ni:
        intensities[j]=ni
        heappush(heap,(ni,j))

  summits=set(summits)
  answer=[-1,float('int')]
  for summit in sorted(summits):
    if intensities[summit]<answer[1]:
      answer=[summit,intensities[summit]]
  return answer

