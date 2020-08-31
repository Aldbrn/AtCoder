n, x, t = map(int, input().split())

ans = t

while True:
  if (n - x) <= 0:
    break
  
  if (n - x) > 0:
    ans += t
    n -= x

print(ans)
