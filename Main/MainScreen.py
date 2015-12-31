#Dhruv Khurana, dkhurana, Section O
from Heroclass import *
from TileClass import *
from Screens import *
from Board import *
from Movement import *
from LevelCreator import *
import pygame 

class MainScreen(object):

    def init(self):
        self.mode="Splash"
        pygame.font.init()
        self.re=False # prevents title screen between levels
        self.highlightText=None 
        self.textPos=None
        self.textArr=["Start","Instructions","Level Creator","Exit"]
        self.font=pygame.font.Font(None,50)
        self.heading=pygame.font.Font(None,32)
        self.instructions=pygame.font.Font(None,27)
        self.textcolor=(250,100,50)
        self.highlightcolor=(250,200,200)
        self.mainScreenColor=(100,20,100)
        self.level=1
        self.image=None
        self.background=None
        self.testLevel=None # actual level arr if using level editor
        self.test=False
        pass

# Template created by Lukas Peraza
# for 15-112 F15 Pygame Optional Lecture, 11/11/15
#Future mouse capability
    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if(keyCode==pygame.K_RETURN):
            if(self.highlightText=="Start"):
                self.mode="Play"
            elif(self.highlightText=="Instructions"):
                self.mode="Instructions"
            elif(self.highlightText=="Level Creator"):
                self.mode="Level Creator"
            elif(self.highlightText=="Exit"):
                pygame.quit()
                exit()

        elif(keyCode==pygame.K_UP):
            if(self.textPos==None):
                self.textPos=3
            else:
                self.textPos-=1
            if(self.textPos==-1):
                self.textPos=3
            self.highlightText=self.textArr[self.textPos]
        elif(keyCode==pygame.K_DOWN):
            if(self.textPos==None):
                self.textPos=0
            else:
                self.textPos+=1
            if(self.textPos==4):
                self.textPos=0
            self.highlightText=self.textArr[self.textPos]
        elif(keyCode==pygame.K_ESCAPE): # go back to splash screen
            self.mode="Splash"
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        if(self.mode=="Level Creator"):
            create=LevelCreator(900,600,50,
                "PyRoads Level Creator",self.testLevel)
            self.mode,self.test,self.testLevel=create.run()
        if(self.mode=="Splash"):
            self.testLevel=None
        if(self.mode=="Play"):
            if(self.test==True): # test level
                play=PygameGame(self.width,
                    self.height,50,"PyRoads",self.testLevel)
                mode=play.run()
                self.mode="Level Creator"
            else: # regular level
                play=PygameGame(self.width,self.height,50,"PyRoads")
                mode=play.run(self.level)
            #go to next level
            if(mode=="Win" and self.level<4 and self.test==False):
                self.level+=1
                self.re=True
            #back to splash screen on losing
            elif((mode=="Fall" or mode=="Dead") and self.test==False):
                self.mode="Splash"
                self.test=False
                self.level=1
            #escape pressed
            elif(mode==None):
                self.mode="Splash"
            self.test=False


    def drawButton(self, screen,highlight,text,pos=0):
        color=self.textcolor
        diffHeight=screen.get_height()//7
        if(highlight==text):
            color=self.highlightcolor
        text=self.font.render(text,
            True,color)
        width=text.get_width()
        height=text.get_height()
        screen.blit(text,(screen.get_width()//2-width//2,
            (screen.get_height()//2)-height//2 + pos*diffHeight))

    def drawBackground(self,screen):
        if(self.background==None):
            image = pygame.image.load("bg2.jpg")
            self.background=pygame.transform.scale(image,(600,400))
        screen.blit(self.background, (0, 0))

    def drawTitle(self,screen):
        if(self.image==None):
            image = pygame.image.load("logo2.png")
            self.image=pygame.transform.scale(image,(900,600))
        screen.blit(self.image, (-50, 0))

    def getRectangleColor(self,num):
        if num==7:
            tile=WinTile()
        elif num==8:
            tile=DeathTile()
        elif num==9:
            tile=SpeedTile()
        elif num==10:
            tile=SlowTile()
        return tile.returnColor()

    def drawInstructions(self,screen):
        lines=["Welcome to PyRoads.",
        "A Journey To Boldly Go Where No Man Has Gone Before",
        "Controls",
        "Arrow keys to move",
        "Space to jump",
        "Escape to go to main screen",
        "Tiles",
        "Win Tile","Death Tile","SpeedUp Tile","Slow Tile"]
        for i in range(len(lines)):
            color=(220,220,255)
            if(i<3 or i==6):
                text=self.heading.render(lines[i],True,color)    
            else:
                text=self.instructions.render(lines[i],True,color)
            width=text.get_width()
            height=text.get_height()
            if(i<3 or i==6):
                screen.blit(text,(screen.get_width()//2-width//2,
                ((screen.get_height()*i)//12)-height//2+ 20))
            else:
                screen.blit(text,(30,
                ((screen.get_height()*i)//12)-height//2+ 20))
                if(i>6):
                    tileColor=self.getRectangleColor(i)
                    pygame.draw.rect(screen,tileColor,((30 + 150),
                        ((screen.get_height()*i)//12-height//2 + 20),25,25))


    def redrawAll(self, screen):
        
        self.drawBackground(screen)
        if (self.mode=="Instructions"):
            self.drawInstructions(screen)
        else:
            
            self.drawButton(screen,self.highlightText,"Start",0)
            self.drawButton(screen,self.highlightText,"Instructions",1)
            self.drawButton(screen,self.highlightText,"Level Creator",2)
            self.drawButton(screen,self.highlightText,"Exit",3)
            self.drawTitle(screen)
        pass

    
    def __init__(self, width=600, height=400, fps=5, title="PyRoads"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)
        bg = pygame.image.load("bg2.jpg")
        bg = pygame.transform.scale(bg,(600,400))
        screen.blit(bg, (0, 0))
        
        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()

        screen.fill((self.mainScreenColor))
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)

                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            if(self.re==False):
                self.redrawAll(screen)
            else:
                self.re=False
            pygame.display.flip()

        pygame.quit()


def main():
    game = MainScreen()
    game.run()

if __name__ == '__main__':
    main()
