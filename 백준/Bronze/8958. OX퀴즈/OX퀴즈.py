import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    result = input()
    score = 0
    cont = 1
    for i in range(len(result)):
        if result[i] == 'O':
            score += cont
            cont += 1
        elif result[i] == 'X':
            cont = 1
    print(score)