x = input().split()
xx = [int(item) for item in x]
if xx[1] > 10:
  row = 10 - xx[0] + 1
  colume = 20 - xx[1] + 1
  print('Left {} {}'.format(row, colume))
else:
  row = 10 - xx[0] + 1
  colume = xx[1]
  print('Right {} {}'.format(row, colume))

		