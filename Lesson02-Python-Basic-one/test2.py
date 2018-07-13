i = 1
j = 1
for i in range(1,6):
    for j in range(1,6):
        if i-j < 1:
            print('*',sep='',end=' ')
        else :
            print(' ',sep='',end='')
    print("")
