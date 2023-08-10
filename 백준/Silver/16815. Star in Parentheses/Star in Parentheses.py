s = input().strip()
stack = []
count = 0
for char in s:
    if not stack and char == "*":
        count = 0
        break
    if char == "(" or char == "*":
        stack.append(char)
    elif char == ")":
        if stack[-1] == "(":
            stack.pop()
        elif stack[-1] == "*":
            stack.append(char)
        else:
            stack.append(char)
    else:
        stack.append(char)
    count = len(stack) // 2
print(count)