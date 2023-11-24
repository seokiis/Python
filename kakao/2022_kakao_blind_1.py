#["muzi", "frodo", "apeach", "neo"]
#["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#2

#[2,1,1,0]

from collections import defaultdict
def solution(id_list, report, k):
  report_dic=defaultdict(list)
  count=defaultdict(int)
  
  for i in report:
    a,b=i.split()
    if(b not in report_dic[a]):
      report_dic[a].append(b)
      count[b]+=1  
  
  answer=[]
  for i in id_list:
    res=0
    for name in report_dic[i]:
      if  count[name]>=k:
        res+=1
    answer.append(res)

  return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))