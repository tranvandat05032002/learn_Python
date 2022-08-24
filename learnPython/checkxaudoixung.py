from math import ceil, floor


x = input()
saveLength = int(len(x))

length = int(len(x) / 2);

if saveLength % 2 == 0:
    if x[0 : length] == x[length : ]:
        print('Xau doi xung')
    else:
        print('Khong la xau doi xung')
else:
    if x[0 : floor(length)] == x[floor(length) + 1 : ] :
        print("xau doi xung")
    else:
        print("khong la xau doi xung")