# 피보나치 N에서 0,1 호출 횟수 = N-1,N-2에서의 0,1 호출 횟수
# 다이나믹 프로그래밍으로 이미 구한 숫자를 또 다시 구하는 일을 없도록 한다.

zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])

    print(zero[num], one[num])


N = int(input())

for i in range(N):
    fibo(int(input()))
