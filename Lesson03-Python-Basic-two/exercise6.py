#exercise1: recursive_1
def f(n):
    #print('n:',n) # Trace recursive levels
    if n==1:
        return 1 
    else:
        return f(n-1)*n
x=int(input("number : "))
for i in range(1,x+1):
    print("F(",i,") : ",f(i))
print('answer: ',f(x))