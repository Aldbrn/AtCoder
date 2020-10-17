import math

n = int(input())
x = list(map(int, input().split()))

for i, n in enumerate(x):
  if n < 0:
    x[i] = n * -1

print(sum(x))

ans = 0
for i in x:
  ans += i ** 2
print(math.sqrt(ans))

print(max(x))