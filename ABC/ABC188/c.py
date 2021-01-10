import numpy as np

n = int(input())
x = int(2 ** n / 2)
a = list(map(int, input().split()))

b = a[x:]
a = a[:x]

if max(a) > max(b):
    print(np.argmax(b) + 1 + x)
else:
    print(np.argmax(a) + 1)
