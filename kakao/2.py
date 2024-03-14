from itertools import chain
from collections import defaultdict

def solution(edges):
  node_array = list(set(chain(*edges)))

  eight_count=0
  one_count=0
  donut_count=0

  node_array2=[0]*(len(node_array))
  for edge in edges:
    node_array2[edge[1]-1]+=1

  node_array3=[0]*(len(node_array))
  for edge in edges:
    node_array3[edge[0]-1]+=1

  answer_node=0
  max_count=0
  for i in range(len(node_array)):
    count=0
    if node_array2[i]==0 and node_array3[i]>0:
      count=node_array3[i]
      if count>max_count:
        max_count=count
        answer_node=i+1
      
  node_array4=[0]*(len(node_array))
  for edge in edges:
    if(edge[0]!=answer_node):
      node_array4[edge[1]-1]+=1

  for i in range(len(node_array)):
    if(node_array4[i]==2 and node_array3[i]==2):
      eight_count+=1
    if(node_array3[i]==0):
      one_count+=1
  
  if(node_array3[answer_node-1]!=(eight_count+one_count)):
    print(node_array3[answer_node-1])
    donut_count=node_array3[answer_node-1]-(eight_count+one_count)

  answer=[]
  answer.append(answer_node)
  answer.append(donut_count)
  answer.append(one_count)
  answer.append(eight_count)
  return answer

solution(

[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])