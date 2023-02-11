a1=int(input("Enter the value of a:"))
a2=int(input("Enter the value of b:"))
a3=int(input("Enter the value of c:"))

import math
h=((y**2)-(4*x*2))

if h==0:

    e=math.sqrt(h)
    x1=(-a2+e)/(2*a1)
    x2=(-a2-e)/(2*a1)
    print("the roots of x is:",x1)
elif h<0:
    print("no result")
else:
    e=math.sqrt(h)
    x1 = (-a2 + e) / (2 * a1)
    x2 = (-a2 - e) / (2 * a1)
    print("the roots of x are:",x1,"and",x2)