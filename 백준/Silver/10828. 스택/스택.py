import sys
input = sys.stdin.readline
N = int(input())
order = []
stack = []
for _ in range(N):
    order.append(input().strip())
for i in range(N):
    if order[i][:2] == "pu":
        stack.append(order[i][5:])
    elif order[i][0] == "t":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    elif order[i][0] == "s":
        print(len(stack))
    elif order[i][0] == "e":
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif order[i][:2] =="po":
        if len(stack) == 0:
            print(-1)
        else:
            pop_num = stack.pop()
            print(pop_num)