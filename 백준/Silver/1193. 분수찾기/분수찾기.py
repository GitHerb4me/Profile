
## 1193
## 분수찾기

import sys
input = sys.stdin.readline

X = int(input())

# step1: 대각선 찾기
line = 1
while X > line:
    X -= line
    line += 1

# step2: 대각선 내에서 위치 찾기
if line % 2 == 0:  # 짝수 대각선 (위 -> 아래)
    a = X
    b = line - X + 1
else:  # 홀수 대각선 (아래 -> 위)
    a = line - X + 1
    b = X

print(f"{a}/{b}")