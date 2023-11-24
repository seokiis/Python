from collections import deque

n=int(input())
graph=[]

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(graph,x,y):
  queue=deque([(x,y)])
  graph[x][y]=0
  count=1

  while queue:
    a,b=queue.popleft()
    for i in range(4):
      na=a+dx[i]
      nb=b+dy[i]

      if na<0 or na>=n or nb<0 or nb>=n:
        continue
      if graph[na][nb]==1:
        graph[na][nb]=0
        queue.append((na,nb))
        count+=1
  return count



for i in range(n):
  graph.append(list(map(int,input().rstrip())))

cnt=[]
for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      cnt.append(bfs(graph,i,j))

cnt.sort()
print(len(cnt))
for i in cnt:
  print(i)

