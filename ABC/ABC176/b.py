n = [int(i) for i in str(int(input()))]

if sum(n) % 9 == 0:
  print("Yes")
else:
  print("No")