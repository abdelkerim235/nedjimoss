a1=int(input("Enter the value of a:"))
a2=int(input("Enter the value of b:"))
a3=int(input("Enter thr value of c:"))
import math
e=math.sqrt((a2**2)-(4*a1*a3))
x1=(-a2+e)/(2*a1)
x2=(-a2-e)/(2*a1)
print("the roots of x are:",x1,"and",x2)