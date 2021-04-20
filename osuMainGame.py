

import logging
import pygame


import osuGamestateManager
import osuMainMenu
import osuGlobals


class MainGame:



    def __init__(self, entryPoint):

        # clear up any unneeded information now that the application has been initialized
        del entryPoint
        logging.info("Successfully cleared all memory relating to the entry point")

        if not pygame.get_init():
            pygame.init()

        # initialize the gamestate of the game
        self.gamestateManager = osuGamestateManager.GameStateManager()
        self.gamestateManager.initializeGamestate(osuMainMenu.GAMESTATE_MainMenu(self.gamestateManager))

        self.mainCanvas = pygame.display.set_mode(osuGlobals.systemResolution)
        

        
            
        self.runMainLoop()


    def runMainLoop(self):

        while(True):
            self.gamestateManager.handleEvents(pygame.event.get())
            
            self.gamestateManager.update()
            # draw the scene (passes the main drawing canvas)
            tempCanvas = pygame.Surface((osuGlobals.osuSettings["Width"],osuGlobals.osuSettings["Height"]))
            self.gamestateManager.draw(tempCanvas)
            tempCanvas = pygame.transform.scale(tempCanvas, (osuGlobals.systemResolution))
            self.mainCanvas.blit(tempCanvas, (0,0))
            pygame.display.update()
        
    




def startMain(entry):

    mainGame = MainGame(entry)
