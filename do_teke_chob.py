import numpy as np
a, b = map(int,input().split())
result = 'NO'
for y in np.arange(0.1,a,0.1):
    x = a - y
    z = b
    if x + y > z and x + z > y and y + z > x:
        result = 'YES'
        print(result)
        break
if result != 'YES':
    for y in np.arange(0.1,b,0.1):
        x = b - y
        z = a
        if x + y > z and x + z > y and y + z > x:
            result = 'YES'
            print(result)
            break   

if result != 'YES':
    print(result)