#判斷座標在第幾象限
x=float(input('請輸入x的座標點'))
y=float(input('請輸入y的座標點'))
if(x>0) :
    if(y>0) :
        print("在第一象限")
    elif(y<0):
        print("在第四象限")
    else :
        print("在x軸上")
elif(x<0) :
    if(y>0) :
        print("在第二象限")
    elif(y<0) :
        print("在第三象限")
    else :
        print("在x軸上")
elif(x==0 and y!=0) :
    print("在y軸上")
else :
    print('在原點')
