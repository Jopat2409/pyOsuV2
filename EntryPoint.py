
import osuGlobals
import importlib

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

        # check the pygame version
        version = pygame.version.vernum
        for i in range(len(version)):
            if not version[i] >= REQUIRED_PYGAME_VERSION[i]:
                return False
        return True

        del pygame

    

    def __init__(self):

        osuGlobals.pygameLatestVersion = self.checkPygame()
        self.getOsuPixelMult()


main = _entryPoint()

    



    

