N, X, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1], arr[y-1] = arr[y-1], arr[x-1]
for i in range(N):
    if arr[i] == X:
        print(i+1)