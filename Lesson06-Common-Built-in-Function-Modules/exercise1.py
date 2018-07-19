def eight_queens(a):
    l = len(a)
    m = 0 
    n = 0
    for i in range(2): #0 is x 1 is y
        for j in range(l): #l is 8 so 0~7
            for k in range(j+1,l): #k is 9 so 1~8
                if a[j][i] == a[k][i]:
                    m += 1

    if m != 0:
        print('False')
    else : 
        for e in range(l-1):
            if (a[e][0]-a[e+1][0]) == (a[e][1]-a[e+1][1]) or (a[e][0]-a[e+1][0]) == -(a[e][1]-a[e+1][1]):
                 n += 1

    if n == 0:
        print('True')
    else :
        print('False')
            


eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])
