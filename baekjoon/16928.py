import sys
from collections import deque

input = sys.stdin.readline

ladder = dict()
snake = dict()

n, s = map(int, input().split())
for i in range(n):
    start, end = map(int, input().split())
    ladder[start] = end
for j in range(s):
    start, end = map(int, input().split())
    snake[start] = end


count = [0] * 101
visited = [0] * 101

queue = deque([1])


while queue:
    now_position = queue.popleft()

    for i in range(1, 7):
        next_position = now_position + i

        # ladder
        if next_position in ladder.keys():
            next_position = ladder[next_position]

        # snake
        if next_position in snake.keys():
            next_position = snake[next_position]

        if next_position <= 100 and not visited[next_position]:
            queue.append(next_position)
            visited[next_position] = 1
            count[next_position] = count[now_position] + 1


print(count[100])
