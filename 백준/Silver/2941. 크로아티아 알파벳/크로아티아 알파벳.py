
def count_croatian_alphabets(text):
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for word in croatia:
        text = text.replace(word, " ")

    return len(text)

data = input()
print(count_croatian_alphabets(data))