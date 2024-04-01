n, m = map(int, input().split())
goods = [input().strip() for _ in range(n)]

start, end = 0, 0
min_length = n + 1
count_e = 0

while end < n:
    if goods[end] == "E":
        count_e += 1
    end += 1

    while count_e >= m:
        min_length = min(min_length, end - start)
        if goods[start] == "E":
            count_e -= 1
        start += 1

if min_length == n + 1:
    print(-1)
else:
    print(min_length)
