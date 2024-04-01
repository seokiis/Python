# 비둘기집 원리
# combinations


# 3
# 3
# ENTJ INTP ESFJ
# 4
# ESFP ESFP ESFP ESFP
# 5
# INFP INFP ESTP ESTJ ISTJ

from itertools import combinations
import sys


def sol(m, n):
    sub_count = 0
    for i in range(4):
        if m[i] != n[i]:
            sub_count += 1
    return sub_count


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 13

    mbti = list(map(str, input().rstrip().split()))

    if n >= 33:
        print(0)
    else:
        case = list(combinations(mbti, 3))
        for a, b, c in case:
            count = 0

            count += sol(a, b)
            count += sol(b, c)
            count += sol(c, a)

            ans = min(ans, count)
        print(ans)
