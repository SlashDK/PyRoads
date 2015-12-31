#Dhruv Khurana, dkhurana, Section O

import pygame
from Heroclass import *
from TileClass import *
from Screens import *
from Board import *
from MainScreen import *


# Template created by Lukas Peraza
# for 15-112 F15 Pygame Optional Lecture, 11/11/15
class PygameGame(object):

    def init(self):
        self.gravity=10
        self.posX=self.width//2
        self.displayTime=0
        self.posYconst=(self.height*2)//3
        self.posY=self.posYconst
        self.size=10
        self.dontWait=False # in case touch death tile
        self.jumpVel=30 # determines jumpheight
        self.t=0
        self.jumpBool=False
        self.speed=10
        self.hero=MoveHero()
        self.speedY=0
        self.count=0
        self.gameOver=False
        pygame.font.init()
        self.font=pygame.font.Font(None,40)
        self.heading=pygame.font.Font(None,45)
        self.stringFont=pygame.font.Font(None,35)
        
        
        pass
    def checkMode(self,surface):
        x=Screens()
        if self.hero.mode=="Win":
            x.win()
            x.draw(surface)
            self.level+=1
            self.gameOver=True

        elif self.hero.mode=="Dead":
            x.lose()
            x.draw(surface)
            self.gameOver=True

        elif self.hero.mode=="Fall":
            self.speedY-=10
            if(self.speedY<=-500): # delay displaying death screen 
            #after finishing falling
                x.lose()
                x.draw(surface)
                self.gameOver=True
        if(self.gameOver==True):
            self.count+=1

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if(keyCode==pygame.K_ESCAPE): # back to splash screen
            self.gameOver=True
            self.dontWait=True
        pass

    def update(self, keysDown):
        if keysDown(pygame.K_LEFT):
            self.hero.move(self,"left")

        if keysDown(pygame.K_RIGHT):
            self.hero.move(self,"right")

        if keysDown(pygame.K_UP) and self.hero.stop==False:
            self.hero.speed+=0.075 # forward acceleration
            self.hero.speed=round(self.hero.speed,2) # helps in debugging
        #and in case python behaves wierdly due to improper float calculations
            if(self.hero.speed>self.hero.maxSpeed):
                self.hero.speed=self.hero.maxSpeed
            
        if keysDown(pygame.K_DOWN):
            self.hero.speed-=0.1
            self.hero.speed=round(self.hero.speed,2) # helps in debugging
        #and in case python behaves wierdly due to improper float calculations
            if(self.hero.speed<0):
                self.hero.speed=0
            
        if keysDown(pygame.K_SPACE):
            self.hero.jump(self)

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        if(self.hero.speed>0):
            self.hero.z+=self.hero.speed # forward movement
            self.hero.z=round(self.hero.z,2)
        
        if(self.jumpBool==True):
            self.t+=0.2 
            self.t=round(self.t,1)
            self.posY=round(self.posYconst-(self.jumpVel*self.t)+
                (0.5*self.gravity*(self.t**2)),3) # simulates gravity

        if(self.posY>self.posYconst): # fix ship to tiles
            self.t=0
            self.jumpBool=False
            self.posY=self.posYconst 
        self.posY-=self.speedY
        self.update(self.isKeyPressed)
        pass

    def levelName(self,screen):
        color=(255,255,255)
        if(self.level==1):
            name="Over the Earth"
        elif(self.level==3):
            name="To the Death Star"
        elif(self.level==2):
            name="Talking to the Moon"
        else:
            name="Test Level"
        text=self.heading.render(name,True,color)
        if(self.displayTime<30):
            screen.blit(text,(screen.get_width()//2-text.get_width()//2,
            (screen.get_height()//2-text.get_height()//2)))
            self.displayTime+=1
        

    def redrawAll(self, screen):
        self.levelName(screen)
        x=pygame.image.load("spaceship.png")
        x=pygame.transform.scale(x,(56,36))
        screen.blit(x, (self.posX-self.size//2,self.posY+self.size//2-5))
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=50,
        title="112 Pygame Game",testLevel=None):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        if(testLevel!=None): # in case of level editor
            self.testLevel=testLevel
        else:
            self.testLevel=None
        pygame.init()

    def drawData(self,screen): # draws data on UI
        color=(100,200,200)
        textGravity=self.font.render(str(self.gravity),True,color)
        textSpeed=self.font.render(str(int(self.hero.speed*20)),True,color)
        if(self.jumpBool):
            textJump=self.stringFont.render("FTW",True,color)
        else:
            textJump=self.stringFont.render("Idle",True,color)
        screen.blit(textSpeed,(screen.get_width()//2-textSpeed.get_width()//2+5,
            (screen.get_height()-57)))
        screen.blit(textGravity,(screen.get_width()//2-110,
            (screen.get_height()-72)))
        screen.blit(textJump,(screen.get_width()//2+82,
            (screen.get_height()-72)))
        pass

    def run(self,level=0):
        self.init()
        self.level=level
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        screen.convert()
        screen.set_colorkey((1,1,1))
        # set the title of the window
        pygame.display.set_caption(self.title)
        if(self.level==1):
            bg = pygame.image.load("bg3.jpg")
        elif(self.level==3):
            bg = pygame.image.load("Deathstar.jpg")
        else:
            bg = pygame.image.load("moon-min.jpg")
        bg=pygame.transform.scale(bg,(600,400))
        screen.blit(bg, (0, 0))
        ui = pygame.image.load("ui2.png")
        ui = pygame.transform.scale(ui,(600,300))
        # stores all the keys currently being held down
        self._keys = dict()
        # call game-specific initialization
        
        playing = True 
        # makes board
        x=Board(self.width,self.height,self.hero,level,self.testLevel)
        self.gravity=x.gravity # level gravity
        while playing:
            screen.blit(bg, (0, 0))
            
            time = clock.tick(self.fps)
            self.timerFired(time)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            
            self.checkMode(screen) # check if win/lose
            if(not self.gameOver):
                x.draw(screen,self.hero.z,self.posX,self.posY,self.posYconst)
                self.redrawAll(screen)
                screen.blit(ui,(0,200))
                self.drawData(screen)
            
            pygame.display.flip()
            if(self.count==35 or self.dontWait):
                break
        return self.hero.mode


def main():
    game = PygameGame()
    game.run()
    
if __name__ == '__main__':
    main()
