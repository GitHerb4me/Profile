import sys
input = sys.stdin.readline

##17404
##RGB거리2

#집의 개수
num_house = int(input())

#input들 행렬로 만들기
cost = []
for _ in range(num_house):
    cost.append(list(map(int, input().split())))

# print(cost)

#컬러별로 최소값이 저장될 빈 리스트
result = []

for first_colour in range(3):

    #dp를 위한 비어있는 칸 만들기
    dp = []
    for i in range(num_house):
        dp.append([0] * 3)
    
    for j in range(3):

        #시작할 첫번째 집과 같은 위치의 dp도 같은 값을 넣기
        if j == first_colour:
            dp[0][j] = cost[0][j]

        #나머지 두개의 집은 엄청 큰 수로 만들어서 다음 줄에서 dp구할 때 고르지 않도록 세팅
        else:
            dp[0][j] = float('inf')

    #dp저장
    for i in range(1, num_house):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]
    
    #첫번째 집과 마지막 집이 달라야 한다. 즉, 이 조건으로 인해 최종적 결과가 result리스트에 담긴다.
    for last_colour in range(3):
        if first_colour != last_colour:
            result.append(dp[-1][last_colour])

#result 리스트에 있는 수 중 가장 최소값 출력
print(min(result))