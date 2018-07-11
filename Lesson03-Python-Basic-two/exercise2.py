#Exercise2: swap
#method1
def f(a,b):
    print("origin : ",a,b)
    c=a
    a=b
    b=c
    print("new :",a,b)
a=int(input("input a number : "))
b=int(input("input a number : "))
f(a,b)
#method2
def w(a,b):
    print("origin : ",a,b)
    a,b=b,a
    print("new :",a,b)
a=int(input("input a number : "))
b=int(input("input a number : "))
w(a,b)