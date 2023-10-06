n = int(input())
m = input()
a = set()
b  = set()
while m != 'HELP':
    x = m.split()
    ans = input()
    if ans == 'YES':
        if len(a) > 0:
            a = a.intersection(set(x))
        else:
            a.update(set(x))
    else:
        b.update(set(x))
    m = input()
a -= b
print(*sorted(a, key=int))