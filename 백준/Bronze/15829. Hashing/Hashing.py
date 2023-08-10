import sys
input = sys.stdin.readline
L = int(input())
word = input()

list = []
for i in range(L):
    list.append(word[i])

sum = 0
for i in range(L):
    sum += (ord(list[i]) - 96) * 31 ** i

print(sum)