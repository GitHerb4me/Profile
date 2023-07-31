import sys
input = sys.stdin.readline

##1149 
##RGB 거리

#집의 개수
num_house = int(input())

#input들 행렬로 만들기
cost = []
for _ in range(num_house):
    cost.append(list(map(int, input().split())))

# print(cost)

#dp를 위한 비어있는 칸 만들기
dp = []
for i in range(num_house):
    dp.append([0] * 3)

# print(dp)

#dp[0] 값에는 cost[0]값 넣기
dp[0] = cost[0]

#dp이용해서 dp값 채우기
for i in range(1, num_house):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

#주어지 3개의 마지막 dp값에서 최소값 출력
print(min(dp[-1]))