import sys
input = sys.stdin.readline

N = int(input())

list = []
for i in range(N):
    s = int(input())
    list.append(s)

list = sorted(list)

for num in list:
    print(num)
   