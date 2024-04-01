import sys
input=sys.stdin.readline

# 분할정복

N,r,c=map(int,input().split())
total_count=0 #4

while N>=1:
  
  N-=1 #1 #0
  one_side_count=(2**N) *(2**N) 
  # 1사분면
  if(c<2**N and r<2**N):
    total_count+=0

  # 2사분면
  elif(c>=2**N and r<2**N):
    total_count+=one_side_count
    c-=2**(N) # r,c = 1,1
    
  #3사분면
  elif(c<2**N and r>=2**N):
    total_count+=2*one_side_count
    r-=2**(N)
    
  #4사분면
  elif(c>=2**N and r>=2**N):
    total_count+=3*one_side_count
    c-=2**(N)
    r-=2**(N)

print(total_count)
  
    

  

  