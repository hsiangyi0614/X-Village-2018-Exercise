x = int(input("enter a number : "))
for i in range(x,0,-1):
    for j in range(x-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print("")
     
