import sys
input=sys.stdin.readline
from collections import deque

#시작점부터 모든 점까지의 거리의 합을 구해야 해
def bfs(graph,start):
  num=[0]*(n+1)
  visited=[start]
  queue=deque([start])

  while queue:
    a=queue.popleft()
    for i in graph[a]:
      if i not in visited:
        num[i]=num[a]+1
        queue.append(i)
        visited.append(i)
  return sum(num)
        

n,m=map(int,input().split())
graph=[[]for _ in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

result=[]
for i in range(1,n+1):
  result.append(bfs(graph,i))

print(result.index(min(result))+1)