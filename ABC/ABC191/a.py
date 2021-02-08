v, t, s, d = map(int, input().split())

sec = d / v
if t > sec or s < sec:
    print("Yes")
else:
    print("No")
