import os
#stores premade game levels

#style function size (25 lines) doesn't apply. 

class Levels(object):
    def __init__(self):
        self.rows=200
        self.cols=9
        self.level = [ ([1] * self.rows) for col in range(self.cols)]
        self.gravity=10

    def level1(self):
        flag=False
        self.rows=100
        self.level = [ ([1] * self.rows) for col in range(self.cols)]
        for j in range(self.rows):
            for i in range(self.cols):
                if (i+j)%2==0:
                    self.level[i][j]=2
            if((j%8==0 or (j-1)%8==0 or (j-2)%8==0) and j>2):
                for i in range(self.cols):
                    self.level[i][j]=10
                if(flag):
                    self.level[2][j]=2
                    self.level[6][j]=2
                else:
                    self.level[3][j]=2
                    self.level[5][j]=2
            else:
                flag=not flag
            if(j%4==0 and j>0 and j%8!=0):
                self.level[2][j]=10
                self.level[6][j]=10
        for i in range(0,100,2):
            if(i>50):
                self.level[0][i]=10
                self.level[8][i]=10
        for j in range(95,100):
            for i in range (self.cols):
                    if (j>95 and self.level[i][j]!=1 ):
                        self.level[i][j]=1
        self.level[4][self.rows-1]=9
        self.level[3][self.rows-1]=9
        self.level[5][self.rows-1]=9
        
    def level2(self):
        self.rows=200
        self.level = [ ([1] * self.rows) for col in range(self.cols)]
        self.gravity=5
        
        for j in range(self.rows):
            for i in range(self.cols):
                if (i+j)%2==0:
                    self.level[i][j]=2
                if(j==199):
                    self.level[i][j]=9
                if(i==2 or i==6):
                    self.level[i][j]=10
                if(j>30 and j<100):
                    if(j>40 and i!=2 and i!= 6):
                        if(((j+1)//20==(j+1)/20 or (j+2)//20==(j+2)/20)):
                                self.level[i][j]=4
                    if(j//20)%2==0:
                        if(i<=5):
                            self.level[i][j]=10
                        elif((j//20==j/20 or (j-1)//20==(j-1)/20) and i>6):
                            self.level[i][j]=3
                        
                    else:
                        if(i>=3):
                            self.level[i][j]=10
                        elif((j//20==j/20 or (j-1)//20==(j-1)/20)
                            and i<2):
                            self.level[i][j]=3
                elif(j>=100 and j<105):
                    self.level[i][j]=10
                elif(j>=105 and j<150):
                    if(j%8==0 or (j+1)%8==0 or (j+2)%8==2):
                        self.level[i][j]=10
                    
                elif(j>=150 and j<190):
                    if(i<3 or i>5):
                        self.level[i][j]=10
                    elif(self.level[i][j]!=9):
                        if((j+i)%2==0):
                            self.level[i][j]=1
                        else:
                            self.level[i][j]=2
                    if(j%20==0 or (j+1)%20==0):
                        self.level[i][j]=10

        pass
    def load(self,filename):
        if os.path.exists('levels'+os.sep+filename):
            file = open('levels'+os.sep+filename,'r')
            string=file.read()
            return eval(string)
    def level3(self):
        self.gravity=7
        self.level=self.load('level3a.pyr')


    def getLevel(self):
        return self.level
    def getGravity(self):
        return self.gravity