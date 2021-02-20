n, k = map(int, input().split())


for i in range(k):
    n = str(n)
    l = list(n)
    l = [int(i) for i in l]
    g1 = sorted(l, reverse=True)
    g2 = sorted(l)
    g1 = int("".join([str(i) for i in g1]))
    g2 = int("".join([str(i) for i in g2]))
    n = g1 - g2

print(n)
