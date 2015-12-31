import pygame
from Heroclass import *
from TileClass import *
from Screens import *
from Levels import *
#gets the level, Draws the board and does the tile action
class Board(object): 
    def __init__(self,width,height,heroObj,getLevel,testLevel=None):
        level=Levels()
        self.getLevel=getLevel
        if(testLevel!=None):
            self.arr=testLevel
        else:
            if(self.getLevel==1):
                level.level1()
            elif(self.getLevel==2):
                level.level2()
            elif(self.getLevel==3):
                level.level3() 
            elif(self.getLevel==0):
                level.level1() 
            self.arr=level.getLevel()
        self.gravity=level.getGravity()
        self.width=width
        self.height=height
        self.cols=10
        self.rows=10
        self.grid=[0*self.cols for i in range (self.rows)]
        self.margin=10
        self.rowHeight=self.height//12
        self.colWidth=self.width//9
        self.tilt=1.6
        self.hero=heroObj
        self.dummyHero=MoveHero()

    def getTile(self,num,col,posX,posY,posYconst,row,level):
        if num==0:
            tile=TileClass()
        elif num==1:
            tile=RegTile(level)
        elif num==2:
            tile=RegTile2(level)
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

        coord=round(self.width/2-(5-col-0.5)*self.colWidth)
        if(((posX>=coord and posX<=coord+self.colWidth)            
            or (posX+30>=coord and posX+30<=coord+self.colWidth))
            and row<5 
            and posY==posYconst
            and num!=10):
            tile.connect(self.hero) # does not empty tile action
        elif(num==10 and ((posX+20>=coord and posX+20<=coord+self.colWidth)            
            or (posX+25>=coord and posX+25<=coord+self.colWidth))
            and row<5
            and posY==posYconst):
            tile.connect(self.hero) # falling (requires to be more on tile)
        return tile.returnColor()

    def draw(self,surf,zPos,posX,posY,posYconst): # draws grid
        screen = pygame.Surface((600,400)) 
        screen.set_colorkey((1,1,1)) 
        screen.fill((1,1,1))
        for row in range(100):
            for column in range(10):
                try:
                    color=self.getTile(self.arr[column][round(row+zPos)//10],
                        column,posX,posY,posYconst,row,self.getLevel)
                except:
                    color=self.getTile(10,column,posX,posY,posYconst,
                        row,self.getLevel)
                    pass
                if(column==9):
                    color=(1,1,1)
                coord=round(self.width/2-(5-column-0.5)*self.colWidth*
                    (1-(row)/100))
                margin=100
                offset=(self.height-2*margin)
                pygame.draw.rect(screen,color,
                    (coord,self.height-row*self.tilt-100,
                    round(self.colWidth*(1-0.001*row)),2) )
        surf.blit(screen, (0,0)) 

        
