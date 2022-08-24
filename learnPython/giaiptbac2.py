from math import *


a = float(input());
b = float(input());
c = float(input());

dental = b**2 - 4*a*c
if dental > 0:
    print(((-b) + sqrt(dental)) / 2*a)
    print(((-b) - sqrt(dental)) / 2*a)
elif dental == 0:
    print(-b/2*a)
else:
    print("pt vo nghiem")