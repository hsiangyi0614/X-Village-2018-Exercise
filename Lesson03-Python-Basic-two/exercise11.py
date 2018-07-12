#
x=int(input("績效評分 : "))
y=int(input("加班時數 : "))
def f(x,y):
    if x > 90 :
        bonus=8000
        overtime_hours=y*200
        month_salary=bonus+overtime_hours
        return month_salary
    elif x >69 :
        bonus=6000
        overtime_hours=y*200
        month_salary=bonus+overtime_hours
        return month_salary
    else :
        bonus=4000
        overtime_hours=y*200
        month_salary=bonus+overtime_hours
        return month_salary
print("月薪  : ",f(x,y))