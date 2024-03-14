import sys
m = int(sys.stdin.readline())
s = set()

# all, empty, remove, check, toggle, add

for i in range(m):
    line = sys.stdin.readline().strip().split()
  

    # all, empty는 따로 처리해준다.
    if len(line) == 1:
        if line[0] == "all":
            s = set({j for j in range(1, 21)})
        else:
            s = set()
    else:
        func, num = line[0], line[1]
        num = int(num)

        if func == "remove":
            s.discard(num)
        elif func == "check":
            print(1 if num in s else 0)
        elif func == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)
        elif func == "add":
            s.add(num)
# set()문법에서 discard는 없는 값을 삭제하려고 하면 그냥 무시한다.
# remove는 없는 값을 삭제하려고 하면 에러가 난다.
