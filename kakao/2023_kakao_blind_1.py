# "2022.05.19"
# ["A 6", "B 12", "C 3"]
# ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
def to_day(data):
  year, month, day=map(int,data.split('.'))
  return year*28*12 + month*28 +day

def solution(today, terms, privacies):
  today=to_day(today)
  months={a[0]:int(a[1:])*28 for a in terms}
  expire=[i+1 for i,privacy in enumerate(privacies)
          if to_day(privacy[:-2]) + months[privacy[-1]]<=today ]
  
  return expire

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))