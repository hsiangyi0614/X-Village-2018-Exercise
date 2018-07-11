#Exercise3: judge_big_lower
#method1
def f(a,b):
    if a==b:
        print("a = b :",a ,"=",b)
    elif a > b:
        print("a > b : ",a ,">",b)
    else :
        print("a < b :",a ,"<",b)
a=int(input("input a number : "))
b=int(input("input a number : "))
f(a,b)
#method2
def w(a,b):
    if a==b:
        result="a = b :",a ,"=",b
        return result
    elif a > b:
        result="a > b : ",a ,">",b
        return result
    else :
        result="a < b :",a ,"<",b
        return result
a=int(input("input a number : "))
b=int(input("input a number : "))
w(a,b)