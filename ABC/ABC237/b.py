h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(list(map(int, input().split())))

ans = list(map(list, zip(*a)))

for i in ans:
    print(*i)
