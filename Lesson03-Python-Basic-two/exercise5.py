#Exercise2: carbon_foot
def rate(x):
    if x=="bus":
        x=0.02
    elif x=="car":
        x=0.24
    elif x=="motor":
        x=0.06
    else :
        x=0
        print("please reset your transportion")
        x=input("交通工具 : ")
    def km(y):
        return x*y
    return km
        
x=input("交通工具 : ")
m=rate(x)
y=float(input("行駛距離 (km/hr): "))
print(m(y))