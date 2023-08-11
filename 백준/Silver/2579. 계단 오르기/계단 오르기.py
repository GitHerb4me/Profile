import sys
input = sys.stdin.readline

N = int(input())

list = []
for i in range(N):
    list.append(int(input()))

dp = [0] * (N + 1)

dp[1] = list[0]
if N > 1:
    dp[2] = list[0] + list[1]
for i in range(3, N + 1):
    dp[i] = max(dp[i-2] + list[i-1], dp[i-3] + list[i-2] + list[i-1])

print(dp[N])