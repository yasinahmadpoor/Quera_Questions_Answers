worodi = input().split()
worodii = [int(x) for x in worodi]
a = 0
b = 0
for i in range(1, worodii[2] + 1) :
    if i % 2 == 0:
      b += worodii[1]
    else:
      a += worodii[0]
print(a + b)
      