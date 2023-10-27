import math

a=int(input())
b=int(input())

area=((a**2)*b)/(4*math.tan(math.pi/b))
print(int(area))