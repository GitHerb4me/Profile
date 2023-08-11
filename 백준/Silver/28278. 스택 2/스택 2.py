import sys
input = sys.stdin.readline
N = int(input())
order = []
stack = []
for _ in range(N):
    order.append(input().strip())
for i in range(N):
    if order[i][0] == "1":
        stack.append(order[i][2:])
    elif order[i][0] == "2":
        if len(stack) == 0:
            print(-1)
        else:
            pop_num = stack.pop()
            print(pop_num)
    elif order[i][0] == "3":
        print(len(stack))
    elif order[i][0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[i][0] == "5":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])