def solution(N,stages):
  #실패율
  fail=[0]*(N+1)
  for i in range(N):
    try:
      fail[i+1]=stages.count(i+1)/sum(1 for stage in stages if stage>=(i+1))
    except:
      fail[i+1]=0
  
  fail=fail[1:]
  answer=sorted(enumerate(fail),key=lambda x:(x[1],-x[0]),reverse=True)
  return [item[0]+1 for item in answer]

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))