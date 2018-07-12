#請撰寫一個程式，能讓使用者猜四個數字，直到正確為止
from string import digits
from random import randint, choice
numStr = '0123456789'
randNum = ''
for i in range(4) :
    n = choice(numStr)
    randNum = randNum + n
    numStr = numStr.replace(n, '')
print ('answer : ',randNum)
#判斷是否都是數字
def isallnumber(num):
    for ch in num :
        if ch not in digits :
            return False
    return True
#判斷是否有相同的字符
def hasSameDigit(sameNum) :
    for i in range(len(sameNum)):
        if (sameNum[0]==sameNum[1]) or (sameNum[0]==sameNum[2]) or (sameNum[0]==sameNum[3]) or (sameNum[1]==sameNum[2]) or (sameNum[1]==sameNum[3]) or (sameNum[2]==sameNum[3]):
            return True
    return False
userNums = []    
results = []
Winner = 0
while Winner == 0:
    num = []
    number = 0
    while (number == 0):
        num = input('輸入四個數字:')
        if (isallnumber(num) == False) :
            print ('***錯誤：您輸入的不是數字，請重新輸入')
            exit
        elif (hasSameDigit(num) == True):
            print ('***錯誤： 請輸入不同數字，請重新輸入')
        elif (len(num) != 4) :
            print ('***錯誤： 請輸入四個數字，請重新輸入')
            exit
            
        else:
            number +=1
    userNum = num
    userNums.append(userNum)