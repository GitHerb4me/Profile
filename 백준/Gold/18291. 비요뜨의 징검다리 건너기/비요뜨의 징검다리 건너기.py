import sys
input = sys.stdin.readline
def power(a,b,m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result
T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(1)
    elif N == 2:
        print(1)
    else:
        print(power(2, N - 2, 1000000007))