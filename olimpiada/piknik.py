#list
lst = list(map(int, input().split(', ')))
#sum
s = sum(lst)
#number of elements
n = int(input())
#print sum and numbers from n to 1
#print(s)
answer = 0

def print_numbers(parts, target):
    current = 0
    found = 0
    for i in lst:
        current += i
        if current == target:
            found += 1
            current = 0
        elif current > target:
            return False
    return current == 0 and found == parts

    
for i in range(n, 0, -1):
   if s % i == 0 and print_numbers(i, s // i):
       answer = i - 1
       break

print(answer)