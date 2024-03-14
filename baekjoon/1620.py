import sys
input=sys.stdin.readline

m,n=map(int,input().split())

pok=[]
for i in range(m):
  pocketmon=input().strip()
  pok.append(pocketmon)

for i in range(n):
  a=input().strip()
  if(a.isdigit()):
    a=int(a)
    print(pok[a-1])
  else:
    print(pok.index(a)+1)



