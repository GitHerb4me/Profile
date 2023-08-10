import sys
input = sys.stdin.readline
K = int(input())
list = []
for _ in range(K):
    list.append(int(input()))
stack = []
for char in list:
    if char != 0:
        stack.append(char)
    else:
        stack.pop()
print(sum(stack))