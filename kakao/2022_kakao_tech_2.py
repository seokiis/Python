from collections import deque

def solution(queue1,queue2):
  s1=sum(queue1)
  s2=sum(queue2)

  if(s1+s2)%2:
    return -1
  
  count=0
  
  #queue1, queue2는 리스트로 주어진다.
  #queue로 만들어주자.
  queue1=deque(queue1)
  queue2=deque(queue2)
  L=len(queue1)

  while count<L*4:
    if s1==s2:
      return count
    elif(s1>s2):
      el=queue1.popleft()
      s1=el
      queue2.append(el)
      s2+=el
      
    else:
      el=queue2.popleft()
      s2-=el
      queue1.append(el)
      s1+=el  
    count+=1

  return -1
  
# 3,2,7,2 | 4,6,5,1
# queue1 pop: 2,7,2 | 4,6,5,1,3
# queue2 pop: 4,3,2,7,2, | 6,5,1