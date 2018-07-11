#終極密碼 － 猜數字
import random
answer = random.randint(1,100)
print(answer)
a=1
b=100
x=int(input("enter a number 1 between 100 :"))
while x!=answer :
    if ( a < x and b > x) :
        if ( x == answer ):
            print("correct : " , x)
        elif ( x > answer) :
            b=x
            print("too big your number right now number ", a ," between ", b)
            x=int(input("enter a number : " ))
        else :
            a=x
            print("too small your number right now number ", a ," between ", b)
            x=int(input("enter a number :"))
    else :
        print("re-enter your number must be in ", a ," between ", b)
        x=int(input("enter a number : " ))
print("correct : " , x)