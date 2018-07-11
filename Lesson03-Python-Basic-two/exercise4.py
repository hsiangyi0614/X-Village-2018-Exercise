#Exercise1: N^X
def number(n):
    def power(x):
        return  n ** x
    return power
n = int(input("input a number : "))
m = number(n)
x=int(input("input a power : "))
print(n,"的",x,"次方 :",m(x))