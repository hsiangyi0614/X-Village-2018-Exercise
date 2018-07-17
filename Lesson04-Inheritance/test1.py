class Car:
    color = None
    __speed = None
    
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed
        
    def boost(self):
        self.speed += 1
        
    def step_break(self):
        self.speed -= 1
        if self.speed < 0:
            self.speed = 0
    def get_speed(self):
        speed = self.speed
        return speed
    def set_speed(self,newspeed):
        
        if (newspeed >100):
            print("your speed is over")
        elif (newspeed < 0):
            print("you no back")
        else :
            print("yoy good")
car = Car("red",100)
print("you car color : ",car.color,"you car speed : ",car.speed)
car.step_break()
car.set_speed(105)
print("you car color : ",car.color,"you car speed : ",car.speed)
