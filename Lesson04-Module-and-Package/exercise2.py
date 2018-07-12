#課程練習：datetime 套件¶
import datetime
#method1
a=datetime.date.today() + datetime.timedelta(days=1)
print(a)

b=datetime.date.today()
print(b)
#method2
def f(y):
    x=y+datetime.timedelta(days=1)
    return x
print(f(b))

today = datetime.date.today()
print("")
tomorrow = today + datetime.timedelta(days=5)
print("tomorrow : ",tomorrow)