n = int(input())
s = list(map(int, input().split()))

count = 0
while all(a % 2 == 0 for a in s):
  s = [a / 2 for a in s]
  count += 1

print(count)