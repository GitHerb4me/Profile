import sys
input = sys.stdin.readline
given_list = list(map(int, input().split()))

if given_list == list(range(1, 9)):
    print("ascending")
elif given_list == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")