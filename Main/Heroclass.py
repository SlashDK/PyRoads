import pygame

class MoveHero(object): # Spaceship
    def __init__(self):
        self.speed=0 # forward speed
        self.z=0 # forward position
        self.maxSpeed=5
        self.mode=None
        self.stop=False

    def mousePressed(self,event, data):
        pass

    def keyPressed(self,event, data):
        pass

    def move(self,data,name):
        if(name=="left"):
            if(data.posX<0): # Failsafe
                self.mode="Fall"
            data.posX-=data.speed

        elif(name=="right"):
            if(data.posX>data.width-25): # Failsafe
                self.mode="Fall"
            data.posX+=data.speed

    def jump(self,data):
        if(data.jumpBool==False):
            data.jumpBool=True
