import sys
input = sys.stdin.readline


# 입력값
input_number = int(input())

# 길이가 input_number 이고 값이 전부 다 무한대인 dp 리스트를 작성
# min을 찾는 dp인데 0으로 세팅하면 항상 최소이므로 정확하게 못찾을 수도 있음
dp = []
for i in range(input_number + 1):
    dp.append(float('inf'))
# input_number가 1일 때 값은 1이므로 여기서도 dp를 사용하려면 dp0 값이 필요하므로 0
dp[0] = 0


for i in range(1, input_number + 1):
    squared_numbers = 1

    #제곱수 전까지만 개수를 센다
    while squared_numbers ** 2 <= i:

        #짜증나는 753과 18의 반례에서 보다싶이 i가 더 작을 때 최솟값이 나오므로 dp[i]가 더 클 때만 바꿔 줄수 있도록 if문 작성
        if dp[i] > dp[i - squared_numbers ** 2] + 1:
            dp[i] = dp[i - squared_numbers ** 2] + 1
        
        #다음 제곱수
        squared_numbers += 1


# 출력
print(dp[input_number])