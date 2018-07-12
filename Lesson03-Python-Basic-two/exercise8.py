#no use function
#加班費計算公式: 每小時可得200元
#績效獎金計算公式：
#績效評分 大於 90分，可得獎金8000元
#績效評分 介於 70~90分，可得獎金6000元
#績效評分 小於 70分，可得獎金4000元
#月薪 ＝ 績效獎金＋加班費
#Question: 請計算員工A, B, C 的月薪。
#員工A: 績效評分：91分, 加班時數20小時
#員工B: 績效評分：75分, 加班時數15小時
#員工C: 績效評分：60分, 加班時數25小時
x=91
y=20
if x > 90 :
    bonus=8000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
elif x >69 :
    bonus=6000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
else :
    bonus=4000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
print("員工A: 績效評分：91分, 加班時數20小時 -->",month_salary)
x=75
y=15
if x > 90 :
    bonus=8000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
elif x >69 :
    bonus=6000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
else :
    bonus=4000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
print("員工B: 績效評分：75分, 加班時數15小時 -->",month_salary)
x=60
y=25
if x > 90 :
    bonus=8000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
elif x >69 :
    bonus=6000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
else :
    bonus=4000
    overtime_hours=y*200
    month_salary=bonus+overtime_hours
print("員工C: 績效評分：60分, 加班時數25小時 -->",month_salary)

