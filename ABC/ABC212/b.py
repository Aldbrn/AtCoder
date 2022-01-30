x = [int(i) for i in input()]

if x[0] == x[1] == x[2] == x[3]:
    print("Weak")
    exit()

for i in range(2):
    if (x[i + 2] - x[i + 1] == 1 or x[i + 2] - x[i + 1] == -9) and (
        x[i + 1] - x[i] == 1 or x[i + 1] - x[i] == -9
    ):
        print("Weak")
        exit()

print("Strong")
