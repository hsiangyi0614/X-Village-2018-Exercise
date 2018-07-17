import random

class Hungryexception(Exception):
    def __init__(self,m):
        self.hunger = str(m)
    def __str__(self):
        return "I'm hungry(Status:" + self.hunger +"),need to eat!"

class Thirstyexception(Exception):
    def __init__(self,n):
        self.thirsty = str(n)
    def __str__(self):
        return "I'm tirsty(Status:" + self.thirsty +"),need to drink!"

class Boredexception(Exception):
    def __init__(self,o):
        self.bor = str(o)
    def __str__(self):
        return "I'm boring(Status:" + self.bor +"),need to play!"

def check(man):
    if man["hunger"]<0:
        raise Hungryexception(man["hunger"])
    if man["water"]<0:
        raise Thirstyexception(man["water"])
    if man["mood"]<0:
        raise Boredexception(man["mood"])

def play(man):
    print("playing...")
    man["hunger"] -= 15
    man["water"] -= 15
    man["mood"] += 5
    check(man)

def eat(man):
    print("eating...")
    man["hunger"] += 5
    check(man)

def drink(man):
    print("drinking...")
    man["water"] += 5
    check(man)
    
actionList = [play, eat, drink]
    
child = {"hunger": 20, "water": 20, "mood": 20}

while True:
    rand = random.randint(0,2)
    try :
        actionList[rand](child)
    except Hungryexception as a:
        #raise HungryException()
        print(a)
        print('eating...')
        break
    except Thirstyexception as b:
        #raise ThirstyException
        print(b)
        print('drinking...')
        break
    except Boredexception as c:
        #raise BoredException
        print(c)
        print('playing...')
        break