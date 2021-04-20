import logging
import pygame
import sys

import pygamePosLib

class GameStateManager:




    def __init__(self):


        self.pausedGamestates = []
        self.c_gamestate = None
        self.c_gameEvents = []

    def initializeGamestate(self, initialGamestate):

        self.c_gamestate = initialGamestate

    def update(self):

        self.c_gamestate.update(self.c_gameEvents)


    def draw(self, graphics):

        # draws the returned canvas onto the main screen adn then updates the screen
        pygamePosLib.blitCenter(self.c_gamestate.draw(), graphics)
        #graphics.blit(self.c_gamestate.draw(), (0,0))
        
        
    def eventMap(self, event, eventMap):
        try:
            eventMap[event]()
        except KeyError:
            pass
        

        
    def handleEvents(self, eventList):

        self.c_gameEvents = []

        #print("Handling Events")

        for event in eventList:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.c_gameEvents.append("mb1")
            elif event.type == pygame.KEYUP:
                try:
                    self.c_gamestate.eventMap[event.key]()
                except KeyError:
                    pass


        
    
    # this method should be used where none of the data relating to the previous gamestate will be needed again soon
    def swapGamestate(self, newGamestate):

        self.c_gamestate.clear()
        self.c_gamestate = newGamestate
        logging.info(f"Successfully switched the gamestate to {newGamestate}")
        

    # this method should be used in the case that the previous gamestate may need to be active again soon
    def pauseGamestate(self, newGamestate):

        self.pausedGamestates.append(self.c_gamestate)
        self.c_gamestate = newGamestate


    # resumes the last paused gamestate
    def resumeLastGamestate(self):

        del self.c_gamestate
        self.c_gamestate = self.pausedGamestates[-1]
        
