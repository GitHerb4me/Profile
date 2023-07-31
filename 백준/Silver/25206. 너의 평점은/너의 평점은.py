grade_point = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_credit = 0.0  # 학점의 총합
total_point = 0.0  # (학점 × 과목평점)의 합

# 20줄에 걸쳐 정보 입력
for _ in range(20):
    _, credit, grade = input().split()
    credit = float(credit)

    # P 등급이 아니라면 계산에 포함
    if grade != 'P':
        total_credit += credit
        total_point += credit * grade_point[grade]

# 전공평점 계산
gpa = total_point / total_credit

print("{:.6f}".format(gpa))