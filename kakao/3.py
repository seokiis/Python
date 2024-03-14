from itertools import combinations
import bisect

def solution(dice):
    temp=[]
    win_global=0

    def add1(cnt):
        for i in range(6):
            temp.append(dice[t1[cnt]][i])
            if cnt+1==len_dice//2:
                t1_sums.append(sum(temp))
            else:
                add1(cnt+1)
            temp.pop()

    def add2(cnt):
        for i in range(6):
            temp.append(dice[t2[cnt]][i])
            if cnt+1==len_dice//2:
                t2_sums.append(sum(temp))
            else:
                add2(cnt+1)
            temp.pop()

    len_dice=len(dice)
    list_ind=[i for i in range(len_dice)]
    ans=[]
    t=list(combinations(list_ind, len_dice//2))
    print("t",t)

    for t1 in t:
        t2=[]
        for i in list_ind:
            if i not in t1:
                t2.append(i)
        print('t1 t2',t1,t2)
        t1_sums=[]
        t2_sums=[]
        add1(0)
        add2(0)
        t1_sums.sort()
        t2_sums.sort()
        print("t1_sum",len(t1_sums))
        print("t2_sum",t2_sums)
        win=0
        for i in t1_sums:
            win+=bisect.bisect_left(t2_sums,i)
        if win>win_global:
            win_global=win
            ans=t1
    ans2=[]
    for i in range(len(ans)):
        ans2.append(ans[i]+1)

    print('ans2',ans2)
    return ans2

solution([[1,2,3,4,5,6],[3,3,3,3,4,4],[1,3,3,4,4,4],[1,1,4,4,5,5]])