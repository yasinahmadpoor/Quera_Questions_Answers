x = input()
y = input()
xx = int(x[::-1])
yy = int(y[::-1])
if xx > yy:
  print(y, " < ", x)
elif xx < yy:
  print(x, " < ", y)
else:
  print(x, " = ", y)


