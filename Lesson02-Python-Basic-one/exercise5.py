# 解找出 1~50 內的所有質數
for i in range(2,50):
    flag = 1
    for j in range(2,i-1):
        if i%j == 0:
            flag = 0
            break
    if (flag==1):
        print(i,end=" ")