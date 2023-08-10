import sys
input = sys.stdin.readline
stick_razer_pos = input().rstrip()
stack = 0
pieces = 0
previous = ""

for char in stick_razer_pos:
    if char == "(":
        stack += 1
    else:
        if previous == "(":
            stack -= 1
            pieces += stack
        else:
            stack -= 1
            pieces += 1
    previous = char
print(pieces)