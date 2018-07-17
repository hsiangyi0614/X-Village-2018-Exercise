from random import randint,choice
numstr = '0123456789'
randnum = ''
for i in range(4):
    n=choice(numstr)
    randnum = randnum + n
    numstr = numstr.replace(n,'')
print("answer : ",randnum)



from string import digits
def samedigits(samenum):
    for i in range(len(samenum)):
        if (samenum[0]==samenum[1]) or (samenum[0]==samenum[2]) or (samenum[0]==samenum[3]) or (samenum[1]==samenum[2]) or (samenum[1]==samenum[3]) or (samenum[2]==samenum[3]):
            return True
        else :
            return False
            
i=0
while i == 0:
    x= str(input("enter four numbers : "))
    if (x!=randnum):
        if (randnum[0]==x[0]) or (randnum[1]==x[1]) or (randnum[2]==x[2]) or (randnum[3]==x[3]) :
            a = '1a'
            if (randnum[0]==x[0]) and (randnum[1]==x[1]) or (randnum[0]==x[0]) and (randnum[2]==x[2]) or (randnum[0]==x[0]) and (randnum[3]==x[3]) or (randnum[1]==x[1]) and (randnum[2]==x[2]) or (randnum[1]==x[1]) and (randnum[3]==x[3]) or (randnum[2]==x[2]) and (randnum[3]==x[3]) :
                a = '2a'
                if (randnum[0]==x[0]) and (randnum[1]==x[1]) and (randnum[2]==x[2]) or (randnum[0]==x[0]) and (randnum[1]==x[1]) and (randnum[3]==x[3]) or (randnum[0]==x[0]) and (randnum[2]==x[2]) and (randnum[3]==x[3]) or (randnum[1]==x[1]) and (randnum[2]==x[2]) and (randnum[3]==x[3]) :
                    a = '3a'
        print (a)            
    else :
        print("you win~~~")
        i += 1
    