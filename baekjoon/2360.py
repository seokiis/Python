import sys
input=sys.stdin.readline

N=int(input())
map=[list(map(int,input().split()))for _ in range(N)]

blue=0
white=0

def solution(x,y,N):
  global white,blue
  color=map[x][y]
  for i in range(x,x+N):
    for j in range(y,y+N):
      if color!=map[i][j]:
        solution(x,y,N//2)
        solution(x,y+N//2,N//2)
        solution(x+N//2,y,N//2)
        solution(x+N//2,y+N//2,N//2)
        return
  if color==0:
    white+=1
  else:
    blue+=1


solution(0,0,N)
print(white)
print(blue)

