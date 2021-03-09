import logging




class GameStateManager:




    def __init__(self):


        self.pausedGamestates = []
        self.c_gamestate = None

    def initializeGamestate(self, initialGamestate):

        self.c_gamestate = initialGamestate

    def update(self):

        self.c_gamestate.update()


    def draw(self, graphics):

        self.c_gamestate.draw(graphics)
    
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
        
