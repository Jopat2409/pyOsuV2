

import importlib
import glob
import os
from datetime import datetime

import logging
# for resolution purposes
import ctypes

import osuGlobals
import osuMainGame

class _entryPoint:

    # This will be the number that all coordinates are multiplied by
    def getOsuPixelMult(self):

        # gets the user resolution in order to resize correctly
        # will need to be changed to accomodate for other users
        user32 = ctypes.windll.user32
        osuGlobals.systemResolution = (user32.GetSystemMetrics(0),user32.GetSystemMetrics(1))

        
        osuGlobals.osuPixelMult = osuGlobals.systemResolution[1] / osuGlobals.OSURES[1]
        print(osuGlobals.osuPixelMult)

        logging.info("Osupixel multiplier successfully calculated!")

    def checkPygame(self):
        if not importlib.util.find_spec('pygame'):
            raise ModuleNotFoundError
        import pygame
            
        REQUIRED_PYGAME_VERSION = (2,0,0)

        # check the pygame version to see which performance functions can and can't be ran by pygame
        version = pygame.version.vernum
        for subV in range(len(version)):
            if not version[subV] >= REQUIRED_PYGAME_VERSION[subV]:
                return False
        return True

        del pygame
        logging.info("Pygame succesfully validated!")


    # load all of the user configs
    def loadUserConfig(self):


        for f in glob.glob("*.cfg"):
            with open(f,encoding="utf-8") as file:
                for line in file:
                    try:
                        k = line.split("=")
                        if line.startswith("key"):
                            lineDict = {k[1].strip(' \t\n\r'):k[0].strip(' \t\n\r')}
                            osuGlobals.osuKeyMap.update(lineDict)
                        else:
                            lineDict = {k[0].strip(' \t\n\r'):k[1].strip(' \t\n\r')}
                            osuGlobals.osuSettings.update(lineDict)
                    except IndexError:
                        logging.warning(f"The line {line} caused some trouble while loading settings!")

        logging.info("File Successfully found and loaded")

                    

        

    def __init__(self):

        # get the current date to create the log file
        dateTime = datetime.now()
        dt_string = dateTime.strftime("%Y-%m-%d-%H-%M-%S")
        # create the log directory if it does not already exist
        if not os.path.isdir('logs'):
            os.mkdir('logs')
        # set up the logger for logging support
        logging.basicConfig(stream=open(f'logs\\{dt_string}.log', 'w', encoding='utf-8'),level=logging.DEBUG)
        # check the pygame version
        osuGlobals.pygameLatestVersion = self.checkPygame()
        # get the multiplier
        self.getOsuPixelMult()
        # load the user's config
        self.loadUserConfig()

        # start the main loop
        osuMainGame.startMain(self)


        


main = _entryPoint()

    



    

