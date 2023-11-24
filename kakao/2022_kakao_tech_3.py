# # DP
# # 현재의 어떤 값을 이용해서 다음에 오는 값을 계산
# # 현재의 알고력, 코딩력을 이용하여 다음 알고력과 코딩력을 계산 => DP

# [alp_req, cop_req, alp_rwd, cop_rwd, cost]
# [[10,15,2,1,2],[20,20,3,3,4]]


def solution(alp,cop, problems):
  #times[알고력][코딩력]
  max_alp=max_cop=0
  for alp_req, cop_req, _,_,_ in problems:
    max_alp=max(max_alp,alp_req)
    max_cop=max(max_cop,cop_req)

  #0 ~ max_alp  
  times=[[float('inf') for _ in range(max_cop+1)] \
          for _ in range(max_alp+1)]
  
  alp=min(alp,max_alp)
  cop=min(cop,max_cop)
  times[alp][cop]=0
  for a in range(alp,max_alp+1):
    for c in range(cop,max_cop+1):
      if(a+1<=max_alp):
        times[a+1][c]=min(times[a+1][c],times[a][c]+1)
      if(c+1<=max_cop):
        times[a][c+1]=min(times[a][c+1],times[a][c]+1)
  
      for alp_req, cop_req, alp_rwd,cop_rwd,cost in problems:
        if a>=alp_req and c>=cop_req:
          na,nc=min(a+alp_rwd,max_alp), min(c+cop_rwd,max_cop)
          times[na][nc]=min(times[na][nc],times[a][c]+cost)
  
  return times[-1][-1]

  

def solution(alp,cop, problems):
  #times[알고력][코딩력]
  max_alp=max_cop=0
  for alp_req, cop_req, _,_,_ in problems:
    max_alp=max(max_alp,alp_req)
    max_cop=max(max_cop,cop_req)

  #0 ~ max_alp  
  times=[[float('inf') for _ in range(max_cop+1)] \
          for _ in range(max_alp+1)]
  
  alp=min(alp,max_alp)
  cop=min(cop,max_cop)
  times[alp][cop]=0
  for a in range(alp,max_alp+1):
    for c in range(cop,max_cop+1):
      if(a+1<=max_alp):
        times[a+1][c]=min(times[a+1][c],times[a][c]+1)
      if(c+1<=max_cop):
        times[a][c+1]=min(times[a][c+1],times[a][c]+1)
  
      for alp_req, cop_req, alp_rwd,cop_rwd,cost in problems:
        if a>=alp_req and c>=cop_req:
          na,nc=min(a+alp_rwd,max_alp), min(c+cop_rwd,max_cop)
          times[na][nc]=min(times[na][nc],times[a][c]+cost)
  
  return times[-1][-1]

  
