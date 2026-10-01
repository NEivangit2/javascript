array_length, number, start, finish = map(int, input().split(', '))
print(array_length)
a = [0] * array_length
print(a)
start -= 1
finish -= 1 
def side_pattern(length):
    b = [0] * length
    if length % 2 == 0:
        for i in range(0, length, 2):
            b[i] = number if i < length - 2 else number - 1
            # if i < length - 2:
            #     b[i] = number
            # else:
            #     b[i] = number - 1
            b[i + 1] = -number
    else:
        for i in range(0, length - 1, 2):
            b[i] = number
            b[i + 1] = -number
    return b

if start == finish:
    a[start] = number
    use_negatife = True
    for i in range(start - 1, -1, -1):
        a[i] = -number if use_negatife else number - 1
        use_negatife = not use_negatife
    use_negatife = True
    for i in range(start + 1, array_length):
        a[i] = -number if use_negatife else number - 1
        use_negatife = not use_negatife
else:
    for i in range(start, finish + 1):
        a[i] = number
    prefix = side_pattern(start)
    sufix = side_pattern(array_length - finish - 1)[::-1]
    a[:start] = prefix
    a[finish + 1:] = sufix
print(a)