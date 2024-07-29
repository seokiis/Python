def solution(N, arr):
    # Character 선언
    Character = {}
    Character["마블"] = [
        "아이언맨",
        "토르",
        "헐크",
        "블랙위도우",
        "캡틴아메리카",
        "캡틴마블",
        "호크아이",
        "그루트",
        "비전",
        "스칼렛위치",
    ]
    Character["짱구"] = [
        "신짱구",
        "신짱아",
        "봉미선",
        "흰둥이",
        "신영식",
        "김철수",
        "한유리",
        "맹구",
        "한수지",
        "채성아",
    ]
    Character["둘리"] = [
        "둘리",
        "도우너",
        "또치",
        "마이콜",
        "고길동",
        "김박사",
        "매머드",
        "램프노인",
        "공실이",
    ]
    Character["뽀로로"] = [
        "뽀로로",
        "크롱",
        "에디",
        "로디",
        "루피",
        "패티",
        "포비",
        "해리",
        "뽀뽀",
        "퉁퉁이",
    ]

    # 분류 처리
    count = {"마블": 0, "짱구": 0, "둘리": 0, "뽀로로": 0, "미분류": 0}
    for name in arr:
        classified = False
        for category in Character:
            if name in Character[category]:
                count[category] += 1
                classified = True
                break
        if not classified:
            count["미분류"] += 1

    # 결과 정렬
    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    result = [category for category, _ in result]

    return result


N = int(input())
Name = list(map(str, input().split()))
answer = solution(N, Name)
for i in answer:
    print(i, end=" ")
