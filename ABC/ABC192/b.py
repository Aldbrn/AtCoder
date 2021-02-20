s = input()

l = []
n = 1
for c in s:
    if n % 2 == 0:
        l.append(c.isupper())
    else:
        l.append(c.islower())
    n += 1

if all(l):
    print("Yes")
else:
    print("No")
