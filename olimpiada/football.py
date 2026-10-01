# x=print()
# y1=print()
# y2=print()
# xy=print()
# yv=print()
x, y1, y2, xv, yv = map(int, input().split(', '))
dy = max(0, y1-yv, yv-y2)
p = abs(x-xv) + dy
print(p)