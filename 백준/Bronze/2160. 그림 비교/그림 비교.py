import sys
input = sys.stdin.readline
N = int(input())
pictures = []
for _ in range(N):
    picture = [input() for _ in range(5)]
    pictures.append(picture)
def diff_count(p1, p2):
    count = 0
    for i in range(5):
        for j in range(7):
            if p1[i][j] != p2[i][j]:
                count += 1
    return count
min_diff = float('inf')
result = (0, 0)
for i in range(N):
    for j in range(i + 1, N):
        diff = diff_count(pictures[i], pictures[j])
        if diff < min_diff:
            min_diff = diff
            result = (i + 1, j + 1)
print(result[0], result[1])