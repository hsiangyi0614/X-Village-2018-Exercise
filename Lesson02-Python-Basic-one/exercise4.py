 #用 * 印出直角三角形
#method1
i = 1
j = 1
while i <= 9:
    while j <= 9:
        if i+j < 7:
            print( '*', sep='', end='\t')
        j += 1
    print("")
    j = 1
    i += 1
#method2
i = 1
j = 1
x = 0
for i in range(1,7):
    x +=1
    for j in range(1,7-x):
        print( '*', sep='', end='\t')
    print("")