#단순 재귀함수
#시간 복잡도 O(2 ** N)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# dp top-down
# 시간 복잡도 O(N)
# 탑다운(메모이제이션) 방식은 '하향식'이라고도 한다.
dp1=[0]*100
def fib1(n):
    if n ==1 or n == 2:
        return 1
    if dp1[n] != 0:
        return dp1[n]
    dp1[n] = fib1(n-1) + fib1(n-2)
    return dp1[n]
    
# dp bottom-up
# DP의 전형적인 형태는 바텀업(Bottom-Up) 방식이다.
# 재귀 호출을 하지 않기 때문에 시간과 메모리 사용량을 줄일 수 있는 장점이 있다.
# 시간 복잡도 O(N)
dp2=[0]*100
def fib2(n):
    dp2[1] = 1
    dp2[2] = 1
    for i in range(3, n+1):
        dp2[i] = dp2[i-1] + dp2[i-2]
    return dp2[n]



