n = int(input())
x = 0
for a in range(1, n):
  for b in range(1, n):
    if a * b < n:
      x += 1
    elif a * b >= n:
      break
print(x)