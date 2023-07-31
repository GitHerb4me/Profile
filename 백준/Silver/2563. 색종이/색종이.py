import sys
input = sys.stdin.readline



#2563

#100 X 100
paper= []
for i in range(100):
    row = []
    for j in range(100):
        row.append(0)
    paper.append(row)

#색종이의 수
number_paper = int(input()) 


for k in range(number_paper):
    x, y = map(int, input().split())

# 색종이 붙이기
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1


# 1인 부분 더하기
result_area = sum(sum(row) for row in paper)

print(result_area)