
import osuGlobals
import importlib

class _entryPoint:


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


    



    

