N = int(input())
count_d = 0
count_p = 0
for _ in range(N):
    now = input()
    if now == "D":
        count_d += 1
    else:
        count_p += 1
    if abs(count_p - count_d) >= 2:
        break
print(f"{count_d}:{count_p}")