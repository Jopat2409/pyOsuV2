import logging
import sys

import osuBeatmapGamestate




class GAMESTATE_MainMenu:


    def __init__(self, gamestateManager):
    
        self.gamestateManager = gamestateManager
        
        self.inputMap = {1:self.play,3:sys.exit}
        logging.info("Initialized main menu gamestate")


    def update(self):

        # temporary text menu to get the program up and running
        
        choice = int(input("What would you like to do? \n 1) Play \n 2) Create \n 3) Quit\n >>> "))
        self.inputMap[choice]()

        
    def play(self):

        self.gamestateManager.swapGamestate(osuBeatmapGamestate.GAMESTATE_BeatmapSelection(self.gamestateManager))



    def draw(self, graphics):

        pass

    def clear(self):

        del self
