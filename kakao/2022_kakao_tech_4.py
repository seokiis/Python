from collections import defaultdict
from heapq import heappop,heappush

def solution(n,paths,gates,summits):
  
  #그래프
  graph=defaultdict(set)
  for i,j,w in paths:
    graph[i].add((j,w))
    graph[j].add((i,w))

  #intensities
  intensities=[float('inf')] *(n+1)

  #heap : intensity, n
  heap=[]

  #시작점 update
  for gate in gates:
    intensities[gate]=0
    heappush(heap,(0,gate))

  while heap:
    i,n=heappop(heap)
    
    if intensities[n]<i or n in summits:
      continue
    
    for j,ji in graph[n]:
      ni=max(i,ji)
      if(intensities[i]>ni):
        intensities[i]=ni
        heappush(heap,(ni,j))
  
  summit=set(summits)
  answer=[-1,float('inf')]
  for summit in sorted(summit):
    if intensities[summit]<answer[1]:
      answer=[summit,intensities[summit]]
  return answer


  

