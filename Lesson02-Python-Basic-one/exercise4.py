 #用 * 印出直角三角形
#method1
i = 1
j = 1
while i <= 9:
    while j <= 9:
        if i+j < 7:
            print( i+j,'*', sep='', end='\t')
        j += 1
    print("")
    j = 1
    i += 1
#method2
i = 1
j = 1
for i in range(1,6):
    print( '* '*(6-i), sep='', end='\t')
    print("")
#method3
x = int(input("enter a number : "))
for i in range(x,0,-1):
    for j in range(x-i):
        print('*',end='')
    for j in range(i):
        print('-',end='')
    print("")
#method4
i = 1
j = 1
x = 0
for i in range(1,7):
    x +=1
    for j in range(1,7-x):
        print('*',sep='',end='\t')
    print("")
#method5
i = 1
j = 1
n = 12
for i in range(1,n):
    for j in range(1,n-i):
        print('*',sep='',end='\t')
    print("")

