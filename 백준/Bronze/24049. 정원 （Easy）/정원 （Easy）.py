N, M = map(int, input().split())
N_flower = list(map(int, input().split()))
M_flower = list(map(int, input().split()))
arr = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    arr[i+1][0] = N_flower[i]
for i in range(M):
    arr[0][i+1] = M_flower[i]
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i-1][j] != arr[i][j-1]:
            arr[i][j] = 1
print(arr[N][M])