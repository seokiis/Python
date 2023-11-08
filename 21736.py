from collections import deque
import sys

input=sys.stdin.readline

N,M=map(int,input().split())
graph=[]
start=()

for i in range(N):
  row=list(input().rstrip())
  for j in range(M):
    if row[j]=='I':
      start=(i,j)
  graph.append(row)

#BFS
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited=[[False]*M for _ in range(N)]

people_count=0 #만날 수 있는 사람 수

queue=deque([start])
visited[start[0]][start[1]]=True
while queue:
  x,y=queue.popleft()
  for i in range(4):
    nx,ny=x+dx[i],y+dy[i]
    #캠퍼스를 벗어나지 않고
    if nx>=0 and nx<N and ny<M and ny>=0:
      #벽이 아니고 방문하지 않은 곳이면 방문
      if graph[nx][ny]!='X' and not visited[nx][ny]:
        queue.append((nx,ny))
        visited[nx][ny]=True

        #사람이면 +1
        if graph[nx][ny]=='P':
          people_count+=1
print(people_count if people_count>0 else 'TT')