x = int(input())
jadwal = []
for n in range(1,x + 2):
  jadwall = [str(y) for y in jadwal]
  print(" ".join(jadwall))
  del jadwal[:]
  for m in range(1,x + 1):
    jadwal.append(n*m)
