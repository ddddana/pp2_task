import time
def sqTime(n,t):
    time.sleep(t/1000)
    return (n**0.5)

n=int(input())
t=int(input())
d=sqTime(n,t)
print(f'Square root of {n} after {t} miliseconds is {d}')
