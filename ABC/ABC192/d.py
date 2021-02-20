# def Base_10_to_n(X, n):
#     if int(X / n):
#         return Base_10_to_n(int(X / n), n) + str(X % n)
#     return str(X % n)


x1 = input()
m = int(input())
x2 = [int(i) for i in x1]

ans = 0
n = max(x2) + 1
while True:
    num = int(x1, int(n))
    if num <= m:
        ans += 1
    else:
        break
    n += 1

print(ans)
