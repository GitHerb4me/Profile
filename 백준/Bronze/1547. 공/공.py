N = int(input())
arr = [i for i in range(1, 4)]
for _ in range(N):
    x, y = map(int, input().split())
    arr[x-1], arr[y-1] = arr[y-1], arr[x-1]
for i in range(3):
    if arr[i] == 1:
        print(i+1)