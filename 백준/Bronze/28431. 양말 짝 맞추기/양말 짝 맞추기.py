cnt = [0] * 10
for _ in range(5):
    num = int(input())
    cnt[num] += 1
    if cnt[num] == 2:
        cnt[num] = 0
for i in range(10):
    if cnt[i] == 1:
        print(i)