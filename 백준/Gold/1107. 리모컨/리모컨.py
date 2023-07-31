import sys
input = sys.stdin.readline

# 원하는 채널(가야하는 채널) N
N = int(input())

# 고장난 버튼의 개수 M
M = int(input())

# 고장난 버튼을 저장하는 broken_num 리스트... 근데 고장난게 하나도 없다면??
if M > 0:
    broken_num = list(input().split())
else:
    broken_num = []  # 고장난게 하나도 없다면 비어있는 리스트로

# 초기값
first_ch = 100


# 가고 싶은 채널에 broken_num 이 있다면 못간다..를 판별해줘야하나?
def possible_ch(ch, broken_num):
    for char in str(ch):
        if char in broken_num:
            return False
    return True


# 카운트를 하기 위한 초기값: + 또는 - 만 사용해서 100에서 N까지 가기 위해 누르는 버튼이 최대이다
# N이 100보다 작으면??
min_count = abs(N - 100)

# possible_ch 뭔가 쓸모있지 않을까 아!그럼 음 원하는 채널 N에 고장나지 않은 번호를 사용한 제일 가까운 수(close_num)를 찾아보자!
# 근데 그 수가 N보다 작을수도 클수도 있잖아..그럼 if문..

# close_num 이 N 보다 클 때,,, 채널은 500,000까지 있지 그럼 0~9까지 다 망가졌을 때 100에서 500,000까지 최대
for i in range(N, N + 500000 + 1):
    # N부터 시작해서 possible_ch를 True 로 반환하는 제일 작은 i를 찾기
    if possible_ch(i, broken_num):
        # 예제 1을 보면 만약 가능한 제일 작은 i가 5490이 나왔을 때 총 클릭한 횟수 일단 4번에다 5490에서 N까지의 거리: 5490 - N
        # 총 클릭한 횟수는 str(len(i)) 사용
        min_count = min(min_count, len(str(i)) + i - N)
        break

# close_num 이 N 보다 작을 때,,,N부터 0까지 거꾸로 가야한다...
for i in range(N, -1, -1):
    # N부터 시작해서 possible_ch를 True 로 반환하는 제일 큰 i 찾기
    if possible_ch(i, broken_num):
        # 위에랑 똑같음
        min_count = min(min_count, len(str(i)) + N - i)
        break

# 출력
print(min_count)