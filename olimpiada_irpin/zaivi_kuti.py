n, k = map(int, input().split())

ans = n * 4

if 2*k <= n:
    ans = n*4
else:
    ans = 8*(n-k)

print(ans)
