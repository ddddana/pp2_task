a = [int(s) for s in input().split()]
b= set()
for n in a:
    if n in b:
        print('YES')
    else:
        print('NO')
        b.add(n)