import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for i in range(n):
    function = input().rstrip()
    number = int(input())
    arr = input().rstrip()[1:-1].split(",")

    queue = deque(arr)
    if number == 0:
        queue = []

    R_count = 0
    D_count = 0
    for alphabet in function:
        if alphabet == "D":
            D_count += 1

    if len(queue) >= D_count:
        for alphabet in function:
            if alphabet == "R":
                R_count += 1
            elif alphabet == "D":

                if R_count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

        # 그대로
        if R_count % 2 == 0:

            print("[" + ",".join(queue) + "]")
        # reverse
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")

    else:
        print("error")
