class Tile(object):
    def __init__(self,level):
        self.num=0
        self.level=level

    def returnColor(self):
        return self.color

    def connect(self,hero):
        hero.stop=False
        pass

class EmptyTile(Tile):
    def __init__(self):
        self.num=10
        self.color=(1,1,1) #colorkey, so transparent

    def connect(self,hero):
        hero.mode="Fall"
        print(hero.z)


class RegTile(Tile):
    def __init__(self,level=1):
        self.num=1
        self.level=level
        if(level==1):
            self.color=(0,100,255)
        elif(level==2 or level==3):
            self.color=(200,250,255)
        else:
            self.color=(0,100,255)


class RegTile2(Tile):
    def __init__(self,level=1):
        self.num=2
        self.level=level
        if(level==1):
            self.color=(255,150,100)
        if(level==2 or level==3):
            self.color=(0,100,255)
        else:
            self.color=(255,150,100)

class SpeedTile(Tile):
    def __init__(self):
        self.num=3
        self.color=(150,255,150)

    def connect(self,hero):
        hero.speed=hero.maxSpeed

class SlowTile(Tile):
    def __init__(self):
        self.num=4
        self.color=(255,100,50)

    def connect(self,hero):
        hero.speed-=0.02
        hero.stop=True
        if(hero.speed<0):
            hero.speed=0

class DeathTile(Tile):
    def __init__(self):
        self.num=8
        self.color=(255,50,10)

    def connect(self,hero):
        hero.mode="Dead"

class WinTile(Tile):
    def __init__(self):
        self.num=9
        self.color=(10,250,10)

    def connect(self,hero):
        hero.mode="Win"
