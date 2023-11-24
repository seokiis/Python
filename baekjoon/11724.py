from collections import deque
import sys

input=sys.stdin.readline

def bfs(graph,start,visited):
  queue=deque([start])
  visited[start]=True

  while queue:
    v=queue.popleft()
    for node in graph[v]:
      if not visited[node]:
        queue.append(node)
        visited[node]=True

n, m=map(int,input().split())
graph=[[]for _ in range(n+1)]
for i in range(m):
  u,v=map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

count=0
visited=[False]*(n+1)
for i in range(1,n+1):
  if not visited[i]:
    bfs(graph,i,visited)
    count+=1

print(count)




