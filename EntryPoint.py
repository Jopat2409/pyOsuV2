
import osuGlobals
import importlib
import glob

# for resolution purposes
from win32api import GetSystemMetrics

class _entryPoint:

    # This will be the number that all coordinates are multiplied by
    def getOsuPixelMult(self):

        osuGlobals.systemResolution = (GetSystemMetrics(0),GetSystemMetrics(1))

        osuGlobals.osuPixelMult = osuGlobals.systemResolution[1] / osuGlobals.OSURES[1]
        print(osuGlobals.osuPixelMult)

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


    def loadUserConfig(self):

        print("Loading user config")

        for f in glob.glob("*.cfg"):
            with open(f,encoding="utf-8") as file:
                for line in file:
                    k = line.split("=")
                    lineDict = {k[1].strip(' \t\n\r'):k[0].strip(' \t\n\r')}
                    if line.startswith("key"):
                        
                        osuGlobals.osuKeyMap.update(lineDict)
                    else:
                        osuGlobals.osuSettings.update(lineDict)

                    


        print(osuGlobals.osuKeyMap)

        

    def __init__(self):

        osuGlobals.pygameLatestVersion = self.checkPygame()
        self.getOsuPixelMult()
        self.loadUserConfig()


        


main = _entryPoint()

    



    

