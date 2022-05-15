def main():
    temp=float(input())
    if temp>=-273 and temp<=6000:
        if temp>100:
            print('Steam')
        elif temp<0:
            print('Ice')
        else:
            print('Water')
main()
      