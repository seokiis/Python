import sys
input=sys.stdin.readline

n=int(input())
arr=(list(map(int,input().split())))

# arr2=sorted(arr)

# O(n*2)
# for i in arr: #O(n)
#   print(arr2.index(i),end='') #O(N)

arr2=sorted(list(set(arr)))
print(arr2)
dic={arr2[i]:i for i in range(len(arr2))}

for i in arr:
  print(dic[i],end=' ')





