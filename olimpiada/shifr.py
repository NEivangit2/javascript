n, m = map(int, input().split(', '))
a = list(map(int, input().split(', ')))
t = input().strip()

def check(start):
    letter_to_number = [None] * 26
    number_to_letter = [None] * 27

    for i in range(m):
        letter = ord(t[i]) - ord('A')
        num = a[start + i]
        mapped = letter_to_number[letter]
        if mapped is not None and mapped != num:
            return None
        owner = number_to_letter[num]
        if owner is not None and owner != letter:
            return None
        letter_to_number[letter] = num
        number_to_letter[num] = letter

    used_nums = {
        letter_to_number[i]
        for i in range(26)
        if letter_to_number[i] is not None
    }
    free_nums = [x for x in range(1, 27) if x not in used_nums]
    fi = 0
    symbol = [0] * 26

    for j in range(26):
        if letter_to_number[j] is not None:
            symbol[j] = letter_to_number[j]
        else:
            symbol[j] = free_nums[fi]
            fi += 1

    return symbol


for i in range(n - m + 1):
    symbol = check(i)
    if symbol is not None:
        print('YES')
        print(*symbol)
        break
else:
    print('NO')