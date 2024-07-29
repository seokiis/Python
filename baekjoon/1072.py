# 10 8

import sys

input = sys.stdin.readline

x, y = map(int, input().split())
# x : 전체
# y : 이긴 횟수


def win_rate(x, y):
    return y * 100 // x


z = y * 100 // x
ans = x


def binary(start, end):

    while start <= end:
        m = (start + end) // 2
        win = win_rate(x + m, y + m)
        if win >= z + 1:
            ans = m
            end = m - 1
        elif win == z:
            start = m + 1
    print(ans)
    exit()


if z >= 99:
    print(-1)
    exit()
else:
    binary(1, x)
