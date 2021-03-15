
import osuGlobals
import importlib
import glob
from datetime import datetime

import logging

# for resolution purposes
from win32api import GetSystemMetrics

import osuMainGame

class _entryPoint:

    # This will be the number that all coordinates are multiplied by
    def getOsuPixelMult(self):

        osuGlobals.systemResolution = (GetSystemMetrics(0),GetSystemMetrics(1))

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

        dateTime = datetime.now()
        dt_string = dateTime.strftime("%d%m%Y%H%M%S")

        logging.basicConfig(stream=open(f'logs\\{dt_string}.log', 'w', encoding='utf-8'),level=logging.DEBUG)

        osuGlobals.pygameLatestVersion = self.checkPygame()
        self.getOsuPixelMult()
        self.loadUserConfig()

        osuMainGame.startMain(self)


        


main = _entryPoint()

    



    

