
from cmath import sqrt


a = int(input());
b = int(input());
c = int(input());
z = float();

z = b*b - 4*a*c;
print(sqrt(z))

if z > 0:
    x1 = float();
    x2 = float();

    x1 = -b + sqrt(z)/ 2*a;
    x2 = -b - sqrt(z)/ 2*a;
    print(x1);
    print(x2);
elif z == 0:
    print((-b)/2*a);
else :
    print("Vo Nhgiem");