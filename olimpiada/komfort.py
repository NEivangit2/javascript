from collections import deque

n, k = map(int, input('').split(', '))
m = list(map(int, input('').split(', ')))


left = 0
answer = 0
for right in range(n):
    print(left, right)
    print(max(m[left:right + 1]))
    while max(m[left:right + 1]) - min(m[left:right + 1]) > k:
        left += 1
    answer = max(answer, right - left + 1)

print(answer)


# result = 0
# left = 0
# min_deque = deque()
# max_deque = deque()
# for right in range(n):
#     while min_deque and m[min_deque[-1]] >= m[right]:
#         min_deque.pop()
#     print(min_deque)
#     min_deque.append(right)
#     while max_deque and m[max_deque[0]] <= m[right]:
#         max_deque.pop()
#     max_deque.append(right)
#     print(max_deque)
#     while m[max_deque[0]] - m[min_deque[0]] > k:
#         if min_deque[0] == left:
#             min_deque.popleft()
#         if max_deque[0] == left:
#             max_deque.popleft()
#         left += 1
#     result = max(result, right - left + 1)
# print(result)