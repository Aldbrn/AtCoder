n, x = map(int, input().split())

m = 0
ans = 0
for _ in range(n):
    v, p = map(int, input().split())
    m += v * p
    ans += 1
    if m > x * 100:
        print(ans)
        exit()

print(-1)
