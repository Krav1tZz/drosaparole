import math

a = int(input("ievadi a"))
b = int(input("ievadi b"))
c = int(input("ievadi c"))

D = b * b - 4* a *c 

if a == 0:
    print("nav kvadratvienadojums")

else:
    x1 = ( -b + math.sqrt(D) ) / 2*a
    x2 = ( -b - math.sqrt(D) ) / 2*a



    if D < 0:
        print("nav saknes")

    elif D == 0:
        print(x1)

    else:
        print(x1, x2)

input()