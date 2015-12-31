import pygame
import time

#draws text in case win/lose

class Screens(object):
    def __init__(self):
        pygame.font.init()
        self.surf = pygame.Surface((600,400))
        self.surf.fill((255,255,255))
        self.surf.set_colorkey((255,255,255)) # make surface transparent
        self.font=pygame.font.Font(None,40)
        self.color=(255,255,254)

    def win(self):
        self.text=self.font.render("Level Complete.",
            False,self.color)
        self.quote=self.font.render("Be with you, the force may.",
            False,self.color)

    

    def lose(self):
        self.text=self.font.render("You Lose.",
            False,self.color)
        self.quote=self.font.render("Time to come to the dark side.",
            False,self.color)
        

    def draw(self,surface):
        xPos=self.surf.get_width()//2-self.text.get_width()//2
        self.surf.blit(self.text,(xPos,200))
        xPos=self.surf.get_width()//2-self.quote.get_width()//2
        self.surf.blit(self.quote,(xPos,350))
        surface.blit(self.surf,(0,0))
        
