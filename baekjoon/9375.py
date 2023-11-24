import sys
input = sys.stdin.readline

a = int(input())

for i in range(a):
    b = int(input())
    wearDict = {}
    for j in range(b):
        wear = list(input().split())
        if wear[1] in wearDict:
            wearDict[wear[1]].append(wear[0])
        else:
            wearDict[wear[1]] = [wear[0]]

    cnt = 1  # 각 종류마다 항목의 개수

    for k in wearDict:
        cnt *= (len(wearDict[k])+1)
    print(cnt-1)
