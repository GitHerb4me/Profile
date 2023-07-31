N = int(input())

count = 0

for _ in range(N):
    word = input()
    
    group_word = True
    used_chars = set()
    prev_char = word[0]
    used_chars.add(prev_char)
    
    for char in word[1:]:
        if char != prev_char:
            if char in used_chars:
                group_word = False
                break
            used_chars.add(char)
            prev_char = char
    
    if group_word:
        count += 1

print(count)