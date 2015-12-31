import pygame
from TileClass import *
import os
import string

class LevelCreator(object):

    def init(self):
        self.cols=9
        self.rows=100
        if(self.level==None): # for coming back after testing level
            self.level = [ ([10] * self.rows) for col in range(self.cols)]
        self.colWidth=30
        self.currTile=10
        self.rowsOnScreen=20
        self.offset=0
        pygame.font.init()
        self.font=pygame.font.Font(None,50)
        self.smallFont=pygame.font.Font(None,25)
        self.textColor=(0,0,255)
        self.textInput=""
        self.takeInput=False
        self.test=False
        self.displayStart=True
        self.displayEnd=False
        pass

    def load(self): # load file
        filename = self.textInput+'.pyr'
        if os.path.exists('levels'+os.sep+filename):
            file = open('levels'+os.sep+filename,'r')
            string=file.read()
            self.level=eval(string)

    def save(self): # save file
        string=repr(self.level)
        filename = self.textInput+'.pyr'
        if os.path.exists('levels'+os.sep+filename):
            print ("File present")
        else:
            file = open('levels'+os.sep+filename,'w')
            file.write(string)
            file.close()
        return

    def mousePressed(self, x, y):
        if(pygame.mouse.get_pressed()):
            self.modifyLevel(x,y)
            if(x>=8*self.colWidth+50 and x<=8*self.colWidth+350 and
                y>=430 and y<=460): # input box
                self.takeInput=True
            elif(x>=8*self.colWidth+50 and x<=8*self.colWidth+190 and
                y>=470 and y<=490): # save box
                self.save()
            elif(x>=8*self.colWidth+210 and x<=8*self.colWidth+350 and
                y>=470 and y<=490): # load box
                self.load()
            elif(x>=8*self.colWidth+50 and x<=8*self.colWidth+350 and
                y>=530 and y<=570): # test box
                self.test=True
            else:
                self.takeInput=False # stop taking input
        pass

    def mouseReleased(self, x, y):
        pass

    def modifyLevel(self,x,y):
        col=x//self.colWidth
        row=y//self.rowHeight
        row=self.rowsOnScreen-row-1+self.offset # since y starts from top
        if(col>=9):
            return
        self.level[col][row]=self.currTile
        pass
    def mouseMotion(self, x, y):
        if(pygame.mouse.get_pressed()):
            self.modifyLevel(x,y)
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if(keyCode==pygame.K_1):
            self.currTile=1
        elif(keyCode==pygame.K_2):
            self.currTile=2
        elif(keyCode==pygame.K_3):
            self.currTile=3
        elif(keyCode==pygame.K_4):
            self.currTile=4
        elif(keyCode==pygame.K_5):
            self.currTile=8
        elif(keyCode==pygame.K_6):
            self.currTile=9
        elif(keyCode==pygame.K_7):#Empty Tile
            self.currTile=10
        elif(keyCode==pygame.K_UP):
            self.offset+=5
            self.displayStart=False
            if(self.offset>self.rows-self.rowsOnScreen):
                self.offset-=5
                self.displayEnd=True
        elif(keyCode==pygame.K_DOWN):
            self.offset-=5
            if(self.offset<=0):
                self.offset=0
                self.displayStart=True
            if(self.displayEnd==True):
                self.displayEnd=False
        elif(keyCode==pygame.K_s): # save shortcut
            self.save()
        elif(keyCode==pygame.K_l): # load shortcut
            self.load()
        if(self.takeInput): # text input for file name
            letter=pygame.key.name(keyCode)
            if(len(letter)==1 and 
                ('z'>=letter>='a' or 
                'Z'>=letter>='A' or
                '9'>=letter>='0')):
                self.textInput+=letter
            elif(letter=="backspace"):
                self.textInput=self.textInput[:-1]


    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def getColor(self,i,j):
        num=self.level[i][j]
        if num==0:
            tile=TileClass()
        elif num==1:
            tile=RegTile()
        elif num==2:
            tile=RegTile2()
        elif num==3:
            tile=SpeedTile()
        elif num==4:
            tile=SlowTile()
        elif num==8:
            tile=DeathTile()
        elif num==9:
            tile=WinTile()
        elif num==10:
            tile=EmptyTile()
        else:
            tile=TileClass(level)#Just in case
        return tile.returnColor()

    def drawGrid(self,screen,rows=20):
        self.rowHeight=self.height//self.rowsOnScreen
        surf = pygame.Surface((screen.get_width(),screen.get_height()))
        surf.set_colorkey((1,1,1))
        surf.fill((1,1,1)) # transparent
        #grid drawing function
        for i in range (self.cols):
            for j in range(self.rowsOnScreen):
                row=self.rowsOnScreen-j-1+self.offset
                pygame.draw.rect(surf,self.getColor(i,row),(i*self.colWidth,
                    j*self.height//self.rowsOnScreen,self.colWidth,
                    self.rowHeight))
                pygame.draw.rect(surf,(0,0,0),(i*self.colWidth,
                    j*self.height//self.rowsOnScreen,self.colWidth,
                    self.rowHeight),1)
        screen.blit(surf,(0,0))
        if(self.displayEnd==True): # display end on level editor
            text=self.smallFont.render("End",True,(1,1,1))
            screen.blit(text,((8*self.colWidth+40),5))
        elif(self.displayStart==True): # display start on level editor
            text=self.smallFont.render("Start",True,(1,1,1))
            screen.blit(text,((8*self.colWidth+40),screen.get_height()-20))
        pass

    def drawInstructions(self,screen):
        spacing=20
        text=self.font.render("Instructions",True,self.textColor)
        width=text.get_width()
        height=text.get_height()
        screen.blit(text,((screen.get_width()//2 + 4*self.colWidth)
            -width//2,spacing*1))
        insText="Press the number of the tile you want to use."
        insText=self.smallFont.render(insText,True,self.textColor)
        screen.blit(insText,((8*self.colWidth+50),spacing*3))
        insText="Click and drag your mouse over the grid to fill in the blocks."
        insText=self.smallFont.render(insText,True,self.textColor)
        screen.blit(insText,((8*self.colWidth+50),spacing*4))
        insText="Use up and down arrow keys to scroll through grid."
        insText=self.smallFont.render(insText,True,self.textColor)
        screen.blit(insText,((8*self.colWidth+50),spacing*5))
        self.drawTiles(screen)
    
    def drawTiles(self,screen):
        startY=150
        space=30
        color=[(0,100,255),(255,150,100),(150,255,150),(255,100,50),
        (255,50,10),(10,250,10),(1,1,1)]
        text=["Regular Tile 1","Regular Tile 2", "SpeedUp Tile","Slow Tile",
        "Death Tile","Win Tile", "Empty"]
        for i in range(7):
            insText=str(i+1)+"."+text[i]
            insText=self.smallFont.render(insText,True,(1,1,1))
            screen.blit(insText,((8*self.colWidth+50),startY+space*i))
            pygame.draw.rect(screen,color[i],(8*self.colWidth+250,
                startY+space*i,20,20),1 if i==6 else 0)

        
    def drawInput(self,screen):
        startY=400
        displayText=self.smallFont.render(self.textInput,True,self.textColor)
        text="File Name"
        text=self.smallFont.render(text,True,self.textColor)
        screen.blit(text,((8*self.colWidth+150),startY))
        pygame.draw.rect(screen,(1,1,1),(8*self.colWidth+50,
                startY+30,300,30),1) # input box
        screen.blit(displayText,((8*self.colWidth+60),startY+37))
        pygame.draw.rect(screen,(1,1,1),(8*self.colWidth+50,
                startY+70,140,20),1) #save box
        pygame.draw.rect(screen,(1,1,1),(8*self.colWidth+50+160,
                startY+70,140,20),1) # load box
        text="Save"
        text=self.smallFont.render(text,True,self.textColor)
        screen.blit(text,((8*self.colWidth+105),startY+71))
        text="Load"
        text=self.smallFont.render(text,True,self.textColor)
        screen.blit(text,((8*self.colWidth+265),startY+71))
        pygame.draw.rect(screen,(1,1,1),(8*self.colWidth+50,
                startY+130,300,40),1)
        text="Test"
        text=self.smallFont.render(text,True,self.textColor)
        screen.blit(text,((8*self.colWidth+200-text.get_width()//2),
            startY+140))
        
        
    def redrawAll(self, screen):
        self.drawGrid(screen)
        self.drawInstructions(screen)
        self.drawInput(screen)
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=900, height=600, fps=50, title="112 Pygame Game",
        level=None):
        self.level=level
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

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (1, 0, 0)):
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
            screen.fill(self.bgColor)
            
            self.redrawAll(screen)
            pygame.display.flip()
            if(self.test):
                return ("Play",self.test,self.level)
        screen = pygame.display.set_mode((600,400)) # splash screen
        return ("Splash",self.test,self.level)


def main():
    game = LevelCreator()
    game.run()

if __name__ == '__main__':
    main()
