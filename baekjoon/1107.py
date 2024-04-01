import sys

input = sys.stdin.readline

target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# broken으로 만들 수 있는 number과 가장 가까운 수를 만들어서 +,-count를 세주자.


count = abs(100 - target)
for nums in range(500000 * 2 + 1):
    nums = str(nums)
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break

        if j == len(nums) - 1:
            count = min(count, abs(int(nums) - target) + len(nums))

print(count)
