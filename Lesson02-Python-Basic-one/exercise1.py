#用公式解解一元二次方程式
a=1
b=2
c=-63
x=(-b+(b*b-4*a*c)**0.5)/2*a
y=(-b-(b*b-4*a*c)**0.5)/2*a
print(x,y)

import math
#a,b,c = (input("輸入一元二次方程式的係數 : ")
# a*x^2+b*x+c=0
a = int(input("輸入一元二次方程式a的係數 : "))
b = int(input("輸入一元二次方程式b的係數 : "))
c = int(input("輸入一元二次方程式c的係數 : "))
d = (b**2-4*a*c)
if d<0 :
    print("no real solution")
elif d==0 :
    x=(-b+math.sqrt(d))/(2*a)
    print("have one soultion : " , x)
else :
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("have two soultion : " , x1 ,"&", x2)