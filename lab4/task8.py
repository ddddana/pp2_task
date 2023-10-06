n = int(input())
s = set([i for i in range(1, n + 1)])
l = input().split()
while "HELP" not in l:
    l = set([int(l[i]) for i in range(len(l))])
    if len(s & l) > len(s - l):
        ans = "YES"
    else:
        ans = "NO"
    print(ans)
    if ans == "YES":
        s = s & l
    else:
        s = s - l
    l = input().split()
s = list(s)
s.sort()
print(*s)