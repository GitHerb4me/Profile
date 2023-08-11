def pascals_triangle(n):
    triangle = [[0]*n for _ in range(n)]
    for i in range(n):
        triangle[i][0] = 1
        triangle[i][i] = 1
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

def triangle_sum(triangle, r, c, w):
    total = 0
    for i in range(w):
        for j in range(i+1):
            total += triangle[r+i-1][c+j-1]
    return total

R, C, W = map(int, input().split())
triangle = pascals_triangle(30)  # 최대 크기를 30으로 설정
print(triangle_sum(triangle, R, C, W))