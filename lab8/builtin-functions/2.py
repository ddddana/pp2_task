s=str(input())
cntup=0
cntlw=0
for ch in s:
    if ch.isalpha():
        if ch.isupper()==True:
            cntup+=1
        else:
            cntlw+=1
print(f"{cntup}")
print(f"{cntlw}")