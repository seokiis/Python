import sys
from collections import deque

input=sys.stdin.readline


# bfs 는 한 단계씩 모든 단계로 커지니까 길이 여러개라도 최솟값을 반환하게 된다. 
def bfs(x,y):
  dx=[0,0,1,-1]
  dy=[1,-1,0,0]

  queue=deque([(x,y)])
  while queue:
    x,y=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      
      #범위 밖
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue

      #벽
      # if graph[nx][ny]==0:
      #   continue 

      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
      
  return graph[n-1][m-1]

n,m=map(int,input().split())
graph=[]

for _ in range(n):
  graph.append(list(map(int,input().rstrip())))

print(bfs(0,0))
