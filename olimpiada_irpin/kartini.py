l, n, w = map(int, input().split())
ans = 0
ans1 = l - n * w
if ans1 % (n + 1) == 0:
    ans = "YES"
else:
    ans = "NO"
print(ans)