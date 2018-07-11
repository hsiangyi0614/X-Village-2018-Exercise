 #用 * 印出直角三角形
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