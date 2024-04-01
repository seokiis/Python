# 3
# 10 12 3 9
# 10 12 7 2
# 13 11 5 6

import sys
input=sys.stdin.readline


def sol(M,N,x,y):
  while x<=M*N:
    if(x-y)%N==0:
      return x
    x+=M
  return-1

n=int(input())

for i in range(n):
  M,N,x,y=map(int,input().split())
  print(sol(M,N,x,y))


      

