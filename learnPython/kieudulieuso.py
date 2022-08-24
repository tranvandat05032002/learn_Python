from decimal import Decimal


from decimal import *
from typing import Type
from unicodedata import decimal
from fractions import *
getcontext().prec = 100;
#decimal
x = 10;
y = 3;
z = Decimal(x) / Decimal(y);

#complex
z1 = 3 + 2j;
z2 = 2 + 3j;

#faction()

tu1 = 3;
mau1 = 5;


print(z);
print(type(z));
print(z1 + z2);
print(type(z1 + z2));
print((z1 + z2).real);
print((z1 + z2).imag);

print(Fraction(tu1, mau1));