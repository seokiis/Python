# 9
# 5 12 7 10 9 1 2 3 11
# 13

# 12 1
# 10 3
# 11 2

# 문제에 단순하게 접근하면 이중 반복문을 이용해야할 것 같지만
# 좌, 우 방향의 인덱스를 이용하여 한 번의 배열 탐색으로 두 수의 합이 x가 되는 쌍을 찾을 수 있다.

import sys

n = int(input())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

answer = 0
left, right = 0, n - 1  # 왼쪽, 오른쪽
while left < right:
    temp = numbers[left] + numbers[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(answer)
