

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

        self.mainCanvas = pygame.display.set_mode((int(osuGlobals.osuSettings["Width"]),
                                                   int(osuGlobals.osuSettings["Height"])))

        
            
        self.runMainLoop()


    def runMainLoop(self):

        while(True):
            self.gamestateManager.handleEvents(pygame.event.get())
            
            self.gamestateManager.update()
            # draw the scene (passes the main drawing canvas)
            self.gamestateManager.draw(self.mainCanvas)
        
    




def startMain(entry):

    mainGame = MainGame(entry)
