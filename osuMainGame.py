

import logging

import osuGamestateManager
import osuMainMenu

class MainGame:



    def __init__(self, entryPoint):

        # clear up any unneeded information now that the application has been initialized
        del entryPoint
        logging.info("Successfully cleared all memory relating to the entry point")


        self.gamestateManager = osuGamestateManager.GameStateManager()
        self.gamestateManager.initializeGamestate(osuMainMenu.GAMESTATE_MainMenu(self.gamestateManager))

        self.runMainLoop()


    def runMainLoop(self):

        while(True):
            self.gamestateManager.update()
            self.gamestateManager.draw("Graphics")
        
    




def startMain(entry):

    mainGame = MainGame(entry)
