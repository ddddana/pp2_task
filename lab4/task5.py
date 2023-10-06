n=input().split()
a = set()
b = set()
for i in range(int(n[0])):
    a.add(int(input()))
for i in range(0,int(n[1])):
    b.add(int(input()))
print(len(a & b))
print(*sorted(a & b))
print(len(a-b))
print(*sorted(a - b))
print(len(b-a))
print(*sorted(b-a))