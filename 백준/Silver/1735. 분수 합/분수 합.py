def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b 
        b = remainder
    return a 
    

A, B = map(int, input().split())
C, D = map(int, input().split())

upper = A * D + C * B  
lower = B * D

gcd_data = gcd(upper, lower)
upper = upper // gcd_data
lower = lower // gcd_data

print(upper, lower)
