num = set()
day = set()
for i in range(3):
  num.update(input())
  a = input().split()
  day.update(a)
print(7 - len(day))
  
      