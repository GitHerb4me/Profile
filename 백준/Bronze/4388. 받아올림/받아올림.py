while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    carry = 0
    count = 0
    while a > 0 or b > 0:
        sum_ab = a % 10 + b % 10 + carry
        if sum_ab >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10
    print(count)
