# 16 4
# noj.am IU
# acmicpc.net UAENA
# startlink.io THEKINGOD
# google.com ZEZE
# nate.com VOICEMAIL
# naver.com REDQUEEN
# daum.net MODERNTIMES
# utube.com BLACKOUT
# zum.com LASTFANTASY
# dreamwiz.com RAINDROP
# hanyang.ac.kr SOMEDAY
# dhlottery.co.kr BOO
# duksoo.hs.kr HAVANA
# hanyang-u.ms.kr OBLIVIATE
# yd.es.kr LOVEATTACK
# mcc.hanyang.ac.kr ADREAMER
# startlink.io
# acmicpc.net
# noj.am
# mcc.hanyang.ac.kr

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}
for _ in range(N):
    a, b = input().split()
    dict[a] = b

for _ in range(M):
    print(dict[input().rstrip()])
