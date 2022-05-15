deg = input().split()
degl = [int(x) for x in deg]
if degl[0] + degl[1] + degl[2] == 180:
  if degl[0] != 0 and degl[1] != 0 and degl[2] != 0:     
    print('Yes')
  else:
    print('No')
else:
    print('No')