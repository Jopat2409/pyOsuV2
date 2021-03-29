import logging
import sys
import pygame
import pygame.gfxdraw

import osuBeatmapGamestate
import osuGlobals

import math




class GAMESTATE_MainMenu:


    def __init__(self, gamestateManager):
    
        self.gamestateManager = gamestateManager
        
        self.inputMap = {1:self.play,3:sys.exit}
        self.eventMap = {}
        logging.info("Initialized main menu gamestate")


    def update(self):

        # temporary text menu to get the program up and running
        pass

        
    def play(self):

        self.gamestateManager.swapGamestate(osuBeatmapGamestate.GAMESTATE_BeatmapSelection(self.gamestateManager))



    def draw(self):

        tempCanvas = pygame.Surface((math.ceil(int(osuGlobals.osuSettings["Height"]) / 2),math.ceil(int(osuGlobals.osuSettings["Height"]) / 2)))
        pygame.gfxdraw.filled_circle(tempCanvas,0,0,math.ceil(int(osuGlobals.osuSettings["Height"]) / 4), (100,100,100))

        return tempCanvas
        

    def clear(self):

        del self
