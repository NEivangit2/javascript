n = int(input())
s1 = [list(map(int, input().split()))for i in range(3)]
print(s1, n)
for t in range(n):
    frets = [s1[i][t] for i in range(3) if s1[i][t] > 0]
    if max(frets) - min(frets) > 3:
        print("No")
        print(t + 1)
        break
else:
    print("Yes")