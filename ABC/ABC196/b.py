x = input()

if "." not in x:
    print(int(x))
else:
    a, b = x.split(".")
    print(int(a))
