kaleme = input()
seda_dar = ['a', 'e','i','o','u']
a = 0
for item in seda_dar:
    a += kaleme.count(item)
if a == 0:
    print(1)
else:
    print(2**a)