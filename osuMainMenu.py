import logging
import sys
import pygame
import pygame.gfxdraw
import pygame.font
import pygamePosLib

import osuBeatmapGamestate
import osuGlobals

import math




class GAMESTATE_MainMenu:


    def __init__(self, gamestateManager):
    
        self.gamestateManager = gamestateManager

        self.largeFont = pygame.font.SysFont('Comic Sans MS', 200)
        self.largeFont.bold = True
        self.osuText = self.largeFont.render("OSU!", True, (255,255,255))
        
        self.inputMap = {1:self.play,3:sys.exit}
        self.eventMap = {}
        self.tempCanvas = pygame.Surface((int(osuGlobals.osuSettings["Width"]),int(osuGlobals.osuSettings["Height"])), pygame.SRCALPHA)

        self.backgroundIMG = pygame.image.load("assets/background.jpg")
        self.backgroundIMG = pygame.transform.scale(self.backgroundIMG, (osuGlobals.osuSettings["Width"], osuGlobals.osuSettings["Height"]))
        


        self.cHeight = math.ceil(int(osuGlobals.osuSettings["Height"]) / 3)

        self.tempX = math.ceil(int(osuGlobals.osuSettings["Width"]) / 2)
        self.tempY = math.ceil(int(osuGlobals.osuSettings["Height"]) / 2)
        self.hover = False
        logging.info("Initialized main menu gamestate")


    def update(self, events):

        mouseX, mouseY = pygame.mouse.get_pos()

        if(mouseX < (self.tempX + self.cHeight) and mouseX > (self.tempX - self.cHeight)) and (mouseY < (self.tempY + self.cHeight) and mouseY > (self.tempY - self.cHeight)):
            self.hover = True
        else:
            self.hover =False
        if "mb1" in events and self.hover:
            self.play()
        


        
    def play(self):

        self.gamestateManager.swapGamestate(osuBeatmapGamestate.GAMESTATE_BeatmapSelection(self.gamestateManager))



    def draw(self):

        self.tempCanvas.blit(self.backgroundIMG, (0,0))
        
        if self.hover:
            pygame.gfxdraw.filled_circle(self.tempCanvas,self.tempX, self.tempY, self.cHeight+50, (200,200,200))
        pygame.gfxdraw.filled_circle(self.tempCanvas,self.tempX, self.tempY, self.cHeight+45, (255,255,255))
        pygame.gfxdraw.filled_circle(self.tempCanvas,self.tempX, self.tempY, self.cHeight, (255,102,170))

        pygamePosLib.blitCenter(self.osuText, self.tempCanvas)

        

        return self.tempCanvas
        

    def clear(self):

        del self
